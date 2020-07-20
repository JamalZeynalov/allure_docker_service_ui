import os
import re
from typing import List

import requests

HOST = os.environ.get('ALLURE_SERVICE_CONTAINER', default='localhost')
BASE_LINK = f"http://{HOST}:5050/allure-docker-service/projects/"


def __is_date(string: str):
    return True if re.match(r'\d{4}-\d{2}-\d{2}', string) else False


def get_latest_daily(limit: int = 10) -> List[str]:
    projects = requests.get(BASE_LINK)
    projects = list(filter(lambda x: __is_date(x), projects.json()['data']['projects']))

    return sorted(projects)[-10:]


def get_all_daily_reports() -> List[str]:
    projects = requests.get(BASE_LINK)
    projects = list(filter(lambda x: __is_date(x), projects.json()['data']['projects']))

    return sorted(projects)
