# import json
# from typing import List
#
# import pandas as pd
#
#
# def get_history_trend(daily_reports: List[str]) -> dict:
#     trend_results = pd.DataFrame()
#     daily_reports = sorted(daily_reports)
#     for project in daily_reports:
#         with open(f'target/projects/{project}/reports/latest/history/history-trend.json') as f:
#             results = json.load(f)[0]['data']
#
#             trend_results.append({
#                 'total': results['total'],
#                 'passed': results['passed'],
#                 'failed': results['failed'],
#                 'broken': results['broken'],
#                 'skipped': results['skipped']
#             }, ignore_index=False)
#
#             trend_results[project] = {
#                 'total': results['total'],
#                 'passed': results['passed'],
#                 'failed': results['failed'],
#                 'broken': results['broken'],
#                 'skipped': results['skipped']
#             }
#     return trend_results
#
#
# trend_results = get_history_trend(["2020-07-11", "2020-07-17"])
# print(trend_results)
