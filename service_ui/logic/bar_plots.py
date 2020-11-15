import json
from datetime import datetime
from typing import List, Optional

import plotly.graph_objects as go
from loguru import logger
from plotly.offline import plot


def __mutate_iso_date(date_string) -> Optional[str]:
    try:
        date_ = datetime.strptime(date_string, "%Y-%m-%d")
        short_date = date_.strftime("%d-%b")

        return short_date
    except ValueError:
        logger.info(
            f"Report {date_string} is cannot be added to the history because it's not ready."
        )


def generate_tests_history_plot(daily_reports: List[str]):
    if not daily_reports:
        no_history = """<div><h1 align='center'>No history available yet. Please upload reports first</h1></div>"""
        return no_history

    # Parse results
    dates = []
    passed = []
    failed = []
    broken = []
    skipped = []
    for project in daily_reports:
        try:
            with open(
                f"service_ui/static/projects/{project}/reports/latest/history/history-trend.json"
            ) as f:
                results = json.load(f)[0]["data"]

                dates.append(project)
                passed.append(results["passed"])
                failed.append(results["failed"])
                broken.append(results["broken"])
                skipped.append(results["skipped"])
        except FileNotFoundError:
            logger.info(f"The report for '{project}' is not generated yet")
            passed.append(0)
            failed.append(0)
            broken.append(0)
            skipped.append(0)

    # Create graph
    fig = go.Figure()
    dates = [__mutate_iso_date(x) for x in dates]

    fig.add_trace(go.Bar(x=dates, y=failed, name="Failed", marker={"color": "red"}))
    fig.add_trace(go.Bar(x=dates, y=broken, name="Broken", marker={"color": "orange"}))
    fig.add_trace(go.Bar(x=dates, y=skipped, name="Skipped", marker={"color": "grey"}))
    fig.add_trace(go.Bar(x=dates, y=passed, name="Passed", marker={"color": "green"}))

    fig.update_layout(
        barmode="stack",
        height=600,
        title={
            "text": "Daily Results History",
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(size=22),
        },
        yaxis_title={"text": "Executed Tests Number", "font": dict(size=14)},
        legend_title={"text": "Filter:", "font": dict(size=14)},
    )

    return plot(fig, output_type="div")
