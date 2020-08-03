import os


class FrontendApp:
    # TODO: Remove
    def __init__(self):
        self.host = os.environ.get('ALLURE_SERVICE_HOST_NAME', default='localhost')
        self.port = f":{port}" if (port := os.environ.get('ALLURE_SERVICE_PORT')) else ':5050'

        self.base_url = f"http://{self.host}{self.port}/allure-docker-service"

    def get_daily_report_url(self, report_date: str):
        return f"{self.base_url}/latest-report?project_id={report_date}"
