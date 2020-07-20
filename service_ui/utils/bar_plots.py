import json
from typing import List

import matplotlib.pyplot as plt
import pandas as pd


def generate_tests_history_plot(daily_reports: List[str]):
    if not daily_reports:
        return
    indexes = []
    passed = []
    failed = []
    broken = []
    skipped = []
    for project in daily_reports:
        try:
            with open(f'target/projects/{project}/reports/latest/history/history-trend.json') as f:
                results = json.load(f)[0]['data']

                indexes.append(project)
                passed.append(results['passed'])
                failed.append(results['failed'])
                broken.append(results['broken'])
                skipped.append(results['skipped'])
        except FileNotFoundError:
            indexes.append(project + '\n (not generated)')
            passed.append(0)
            failed.append(0)
            broken.append(0)
            skipped.append(0)

    plotdata = pd.DataFrame({
        "failed": failed,
        "broken": broken,
        "skipped": skipped,
        "passed": passed,
    }, index=indexes)

    # Generate report
    plotdata.plot.bar(stacked=True, rot="horizontal",
                      color=['red', 'orange', 'grey', 'green'],
                      figsize=(16, 6))

    plt.title("Daily History",
              fontdict={'family': 'serif', 'weight': 'normal', 'size': 16})
    plt.ylabel("Executed test cases count",
               fontdict={'weight': 'normal', 'size': 12})

    # Save it to a temporary buffer.
    plt.savefig('./service_ui/static/trending.png', format="png")
