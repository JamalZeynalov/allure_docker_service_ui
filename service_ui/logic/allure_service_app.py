import os

import requests
from django.http import HttpResponse


class AllureServiceApp:
    """ A client for Allure Docker Service running application.
    """

    def __init__(self):
        self.host = os.environ.get("ALLURE_SERVICE_HOST_NAME", default="localhost:5050")
        self.port = (
            f":{port}" if (port := os.environ.get("ALLURE_SERVICE_PORT")) else ""
        )

        self.base_url = f"http://{self.host}{self.port}/allure-docker-service"

    def get_projects(self) -> dict:
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

    def delete_project(self, project_id: str) -> HttpResponse:
        """ Delete project by ID
        """
        response = requests.delete(f"{self.base_url}/projects/{project_id}")
        assert response.status_code == 200, (
            f"Cannot delete projects. " f"Response:\n {response.content}"
        )

        return HttpResponse(status=response.status_code, content=response.content)
