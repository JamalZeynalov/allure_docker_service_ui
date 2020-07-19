import json
from typing import List

import matplotlib.pyplot as plt
import pandas as pd


def generate_tests_history_plot(daily_reports: List[str]):
    indexes = []
    passed = []
    failed = []
    broken = []
    skipped = []

    for project in daily_reports:
        with open(f'target/projects/{project}/reports/latest/history/history-trend.json') as f:
            results = json.load(f)[0]['data']

            indexes.append(project)
            passed.append(results['passed'])
            failed.append(results['failed'])
            broken.append(results['broken'])
            skipped.append(results['skipped'])

    plotdata = pd.DataFrame({
        "failed": failed,
        "broken": broken,
        "skipped": skipped,
        "passed": passed,
    }, index=indexes)

    # Generate report
    plotdata.plot.bar(stacked=True, rot="horizontal",
                      color=['red', 'orange', 'grey', 'green'])
    plt.title("Daily History")
    plt.xlabel("Daily Reports")
    plt.ylabel("Test cases")

    # Save it to a temporary buffer.
    plt.savefig('./service_ui/static/trending.png', format="png")
