import os

import requests


class BackendApp:
    def __init__(self):
        self.host = os.environ.get('ALLURE_SERVICE_HOST', default='localhost:5050')
        self.port = f":{port}" if (port := os.environ.get('ALLURE_SERVICE_PORT')) else ''

        self.base_url = f"http://{self.host}{self.port}/allure-docker-service"

    def get_projects(self):
        response = requests.get(f"{self.base_url}/projects")
        assert response.status_code == 200, f"Cannot get projects from API. Response:\n {response.content}"

        return response.json()['data']['projects']
