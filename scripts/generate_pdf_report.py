#!/usr/bin/env python3
"""
README Roast — PDF Report Generator

Generates a professional PDF report from README audit data.
Requires: pip install reportlab

Usage:
    python3 generate_pdf_report.py <input.json> <output.pdf>
"""

import json
import sys
import os
from datetime import datetime

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, mm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        PageBreak, HRFlowable
    )
    from reportlab.graphics.shapes import Drawing, Rect, String, Circle, Wedge
    from reportlab.graphics.charts.barcharts import VerticalBarChart
    from reportlab.graphics import renderPDF
except ImportError:
    print("ERROR: reportlab is not installed. Run: pip install reportlab")
    sys.exit(1)

# Color palette
NAVY = colors.HexColor("#1a1a2e")
BLUE = colors.HexColor("#0f3460")
GREEN = colors.HexColor("#00b894")
YELLOW = colors.HexColor("#fdcb6e")
RED = colors.HexColor("#e17055")
CORAL = colors.HexColor("#e94560")
LIGHT_GRAY = colors.HexColor("#f5f6fa")
DARK_GRAY = colors.HexColor("#636e72")
WHITE = colors.white


def score_color(score):
    if score >= 80:
        return GREEN
    elif score >= 60:
        return BLUE
    elif score >= 40:
        return YELLOW
    else:
        return RED


def score_label(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 55:
        return "Fair"
    elif score >= 40:
        return "Needs Work"
    else:
        return "Critical"


def draw_score_gauge(score, width=200, height=120):
    """Draw a semicircular score gauge."""
    d = Drawing(width, height)
    cx, cy = width / 2, 30
    radius = 60

    # Background arc (gray)
    d.add(Wedge(cx, cy, radius, 0, 180, fillColor=LIGHT_GRAY, strokeColor=None))

    # Score arc (colored)
    angle = (score / 100) * 180
    d.add(Wedge(cx, cy, radius, 0, angle, fillColor=score_color(score), strokeColor=None))

    # Inner circle (white, to create donut effect)
    d.add(Wedge(cx, cy, radius * 0.6, 0, 180, fillColor=WHITE, strokeColor=None))

    # Score text
    d.add(String(cx, cy + 10, f"{score}", fontSize=28, fontName="Helvetica-Bold",
                 fillColor=NAVY, textAnchor="middle"))
    d.add(String(cx, cy - 5, "/100", fontSize=12, fontName="Helvetica",
                 fillColor=DARK_GRAY, textAnchor="middle"))
    d.add(String(cx, height - 10, score_label(score), fontSize=14,
                 fontName="Helvetica-Bold", fillColor=score_color(score),
                 textAnchor="middle"))

    return d


def draw_bar_chart(data, categories, width=450, height=200):
    """Draw a bar chart comparing scores vs category averages."""
    d = Drawing(width, height)
    bc = VerticalBarChart()
    bc.x = 50
    bc.y = 30
    bc.height = height - 60
    bc.width = width - 80
    bc.data = data
    bc.categoryAxis.categoryNames = categories
    bc.categoryAxis.labels.fontName = "Helvetica"
    bc.categoryAxis.labels.fontSize = 8
    bc.categoryAxis.labels.angle = 0
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = 100
    bc.valueAxis.valueStep = 20
    bc.bars[0].fillColor = CORAL
    if len(data) > 1:
        bc.bars[1].fillColor = BLUE
    bc.barWidth = 15
    bc.groupSpacing = 15
    d.add(bc)
    return d


def build_pdf(data, output_path):
    """Build the complete PDF report."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="Title2",
        parent=styles["Title"],
        fontSize=24,
        textColor=NAVY,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name="Subtitle",
        parent=styles["Normal"],
        fontSize=12,
        textColor=DARK_GRAY,
        spaceAfter=20
    ))
    styles.add(ParagraphStyle(
        name="SectionHead",
        parent=styles["Heading2"],
        fontSize=16,
        textColor=NAVY,
        spaceBefore=20,
        spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name="BodyText2",
        parent=styles["Normal"],
        fontSize=10,
        textColor=NAVY,
        spaceAfter=8,
        leading=14
    ))

    elements = []

    # --- Cover Page ---
    elements.append(Spacer(1, 80))
    elements.append(Paragraph("README Roast", styles["Title2"]))
    elements.append(Paragraph("Star Conversion Audit Report", styles["Subtitle"]))
    elements.append(Spacer(1, 20))

    repo_name = data.get("repo_name", "Unknown")
    repo_url = data.get("repo_url", "")
    stars = data.get("stars", 0)
    category = data.get("category", "unknown")
    date = data.get("date", datetime.now().strftime("%Y-%m-%d"))
    readme_score = data.get("readme_score", 0)

    info_data = [
        ["Repository", repo_name],
        ["URL", repo_url],
        ["Stars", str(stars)],
        ["Category", category.replace("-", " ").title()],
        ["Date", date],
    ]
    info_table = Table(info_data, colWidths=[120, 350])
    info_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("TEXTCOLOR", (0, 0), (-1, -1), NAVY),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
    ]))
    elements.append(info_table)
    elements.append(Spacer(1, 30))

    # Score gauge
    gauge = draw_score_gauge(readme_score)
    elements.append(gauge)
    elements.append(Spacer(1, 20))

    elements.append(PageBreak())

    # --- Score Dashboard ---
    elements.append(Paragraph("Score Dashboard", styles["SectionHead"]))
    elements.append(HRFlowable(width="100%", thickness=1, color=NAVY))
    elements.append(Spacer(1, 10))

    scores = data.get("scores", {})
    cat_avgs = data.get("category_averages", {})
    weight_map = {
        "hero": ("Hero & Value Prop", 0.25),
        "visuals": ("Visual Proof", 0.20),
        "install": ("Install & Quickstart", 0.15),
        "trust": ("Trust Signals", 0.15),
        "structure": ("Structure & Scannability", 0.15),
        "differentiation": ("Differentiation & CTA", 0.10),
    }

    table_data = [["Category", "Score", "Weight", "Weighted", "vs. Avg"]]
    for key, (label, weight) in weight_map.items():
        score = scores.get(key, 0)
        avg = cat_avgs.get(key, 0)
        weighted = round(score * weight, 1)
        delta = score - avg
        delta_str = f"+{delta}" if delta >= 0 else str(delta)
        table_data.append([label, f"{score}/100", f"{int(weight*100)}%",
                          str(weighted), delta_str])

    table_data.append(["TOTAL", "", "", f"{readme_score}/100", ""])

    score_table = Table(table_data, colWidths=[160, 70, 60, 70, 70])
    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, -1), (-1, -1), LIGHT_GRAY),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, DARK_GRAY),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(score_table)
    elements.append(Spacer(1, 20))

    # Bar chart: You vs Category Average
    chart_categories = [label[:12] for _, (label, _) in weight_map.items()]
    your_scores = [scores.get(k, 0) for k in weight_map.keys()]
    avg_scores = [cat_avgs.get(k, 0) for k in weight_map.keys()]
    chart = draw_bar_chart([your_scores, avg_scores], chart_categories)
    elements.append(Paragraph("Your Scores vs. Category Average", styles["BodyText2"]))
    elements.append(chart)
    elements.append(Paragraph(
        '<font color="#e94560">■</font> Your README &nbsp;&nbsp;'
        '<font color="#0f3460">■</font> Category Average',
        styles["BodyText2"]
    ))

    elements.append(PageBreak())

    # --- Star Killers ---
    elements.append(Paragraph("Star Killers", styles["SectionHead"]))
    elements.append(HRFlowable(width="100%", thickness=1, color=CORAL))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        "These are the issues most likely reducing your star conversion, "
        "ranked by the gap between your score and the category average.",
        styles["BodyText2"]
    ))
    elements.append(Spacer(1, 10))

    for i, killer in enumerate(data.get("star_killers", [])[:5], 1):
        cat_name = killer.get("category", "Unknown")
        gap = killer.get("gap", 0)
        fix = killer.get("fix", "")
        elements.append(Paragraph(
            f"<b>{i}. {cat_name}</b> — {gap} points below average",
            styles["BodyText2"]
        ))
        elements.append(Paragraph(f"Fix: {fix}", styles["BodyText2"]))
        elements.append(Spacer(1, 6))

    elements.append(PageBreak())

    # --- Pattern Gaps ---
    patterns = data.get("patterns", {})
    pattern_benchmarks = data.get("pattern_benchmarks", {})
    if patterns or pattern_benchmarks:
        elements.append(Paragraph("Pattern Gaps vs. Category", styles["SectionHead"]))
        elements.append(HRFlowable(width="100%", thickness=1, color=BLUE))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph(
            "How your README compares to what top repos in your category have.",
            styles["BodyText2"]
        ))
        elements.append(Spacer(1, 8))

        pattern_labels = {
            "has_gif": "GIF/Video Demo",
            "has_screenshot": "Screenshot",
            "has_demo_link": "Live Demo Link",
            "has_comparison_table": "Comparison Table",
            "has_used_by": "\"Used By\" Section",
            "has_toc": "Table of Contents",
            "has_quickstart_output": "Quickstart Output Shown",
            "has_community_link": "Community Link",
            "has_contributing": "Contributing Guide",
            "has_license_badge": "License Badge",
        }

        gap_data = [["Pattern", "You", "% of Top Repos", "Gap?"]]
        for key, label in pattern_labels.items():
            has_it = patterns.get(key, False)
            pct = pattern_benchmarks.get(key, 0)
            you_str = "Yes" if has_it else "No"
            gap_str = "" if has_it else ("Yes" if pct >= 40 else "Minor")
            gap_data.append([label, you_str, f"{pct}%", gap_str])

        if len(gap_data) > 1:
            gap_table = Table(gap_data, colWidths=[160, 50, 110, 60])
            gap_table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (1, 0), (-1, -1), "CENTER"),
                ("GRID", (0, 0), (-1, -1), 0.5, DARK_GRAY),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]))
            elements.append(gap_table)

        elements.append(PageBreak())

    # --- Score Projection ---
    projection = data.get("score_projection", {})
    if projection:
        elements.append(Paragraph("Score Projection", styles["SectionHead"]))
        elements.append(HRFlowable(width="100%", thickness=1, color=GREEN))
        elements.append(Spacer(1, 10))

        proj_data = [["Milestone", "Score", "Key Change"]]
        for milestone in projection:
            proj_data.append([
                milestone.get("milestone", ""),
                f"{milestone.get('score', 0)}/100",
                milestone.get("change", ""),
            ])

        proj_table = Table(proj_data, colWidths=[140, 80, 250])
        proj_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("ALIGN", (1, 0), (1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 0.5, DARK_GRAY),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        elements.append(proj_table)
        elements.append(Spacer(1, 10))

    # --- Action Plan ---
    elements.append(Paragraph("Action Plan", styles["SectionHead"]))
    elements.append(HRFlowable(width="100%", thickness=1, color=GREEN))
    elements.append(Spacer(1, 10))

    for section_name, section_key, color in [
        ("Quick Wins (< 1 hour each)", "quick_wins", GREEN),
        ("This Weekend", "medium_term", BLUE),
        ("When You're Ready", "strategic", DARK_GRAY),
    ]:
        items = data.get(section_key, [])
        if items:
            elements.append(Paragraph(f"<b>{section_name}</b>", styles["BodyText2"]))
            for item in items:
                elements.append(Paragraph(f"• {item}", styles["BodyText2"]))
            elements.append(Spacer(1, 12))

    # --- Footer ---
    elements.append(Spacer(1, 30))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=DARK_GRAY))
    elements.append(Paragraph(
        f"Generated by README Roast — {date}",
        ParagraphStyle("Footer", parent=styles["Normal"], fontSize=8,
                       textColor=DARK_GRAY, alignment=1)
    ))

    doc.build(elements)
    return output_path


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 generate_pdf_report.py <input.json> <output.pdf>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r") as f:
        data = json.load(f)

    result = build_pdf(data, output_path)
    size = os.path.getsize(result)
    print(f"PDF generated: {result} ({size:,} bytes)")


if __name__ == "__main__":
    main()
