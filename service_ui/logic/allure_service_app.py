import os

import requests


class AllureServiceApp:
    """ A client for Allure Docker Service running application.
    """

    def __init__(self):
        self.host = os.environ.get("ALLURE_SERVICE_HOST_NAME", default="localhost:5050")
        self.port = (
            f":{port}" if (port := os.environ.get("ALLURE_SERVICE_PORT")) else ""
        )

        self.base_url = f"http://{self.host}{self.port}/allure-docker-service"

    def get_projects(self):
        """ Get all reports from Allure Docker Service
        """
        try:
            response = requests.get(f"{self.base_url}/projects")
            assert response.status_code == 200, (
                f"Cannot get projects from API. " f"Response:\n {response.content}"
            )

            return response.json()["data"]["projects"]
        except requests.exceptions.ConnectionError:
            return {}
