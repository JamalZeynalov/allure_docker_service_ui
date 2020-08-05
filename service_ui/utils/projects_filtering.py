import re
from os.path import isfile
from typing import List

from service_ui.utils.backend_app import BackendApp


def __is_date(string: str):
    return True if re.match(r'\d{4}-\d{2}-\d{2}', string) else False


def get_all_daily_reports() -> List[str]:
    projects = BackendApp().get_projects()
    filtered = list(filter(lambda x: __is_date(x), projects))

    return sorted(filtered)


def get_latest_daily(limit: int = 10) -> List[str]:
    return get_all_daily_reports()[-limit:]


def get_report_path_if_exists(report_date: str):
    path = f"projects/{report_date}/reports/latest/index.html"
    full_path = f"./service_ui/static/{path}"

    return 'work-in-progress.png' if not isfile(full_path) else path
