import re
from os.path import isfile
from typing import List

from service_ui.logic.allure_service_app import AllureServiceApp


def __is_date(string: str) -> bool:
    """ Check if a string is in format "YYY-MM-DD"
    :param string: source string
    """
    return True if re.match(r"\d{4}-\d{2}-\d{2}", string) else False


def get_all_daily_reports() -> List[str]:
    """ Get all reports whose identifiers match the "YYYY-MM-DD" pattern
    :return: sorted list of reports IDs
    """
    projects = AllureServiceApp().get_projects()
    filtered = list(filter(lambda x: __is_date(x), projects))

    return sorted(filtered)


def get_latest_daily(limit: int = 10) -> List[str]:
    """ Get identifiers of latest available daily reports
    :param limit: number of returned identifiers
    :return: List of report IDs
    """
    return get_all_daily_reports()[-limit:]


def get_report_path_if_exists(report_date: str) -> str:
    """ Get a link to the HTML report to be embedded in the iframe
    :param report_date: string in format "YYY-MM-DD"
    :return: A path to the HTML report index if it exists,
             otherwise return a link to 'work-in-progress.png'
    """
    path = f"projects/{report_date}/reports/latest/index.html"
    full_path = f"./service_ui/static/{path}"

    return "work-in-progress.png" if not isfile(full_path) else path
