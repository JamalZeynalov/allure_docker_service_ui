import base64
import json
import os
from datetime import datetime

import requests


def send_results(service_url: str, results_directory, project_id: str = None) -> None:
    """
    :param project_id: should contains alphanumeric lowercase characters or hyphens
    :param results_directory: Absolute path to the allure results directory
           where you have all your results locally, generally this directory is named as `allure-results`
           Example: 'C:\\Users\\<User>\\<project>\\target\\allure-results\\target\\allure-results'
    :param service_url: allure-docker-service URL
    """
    # Results will be send with current date as project_id.
    # Old tests results will be re-written during the day.
    project_id = project_id if project_id else datetime.today().strftime("%Y-%m-%d")

    # This url is where the Allure container is deployed
    allure_service_api_url = f"{service_url}/allure-docker-service"

    print("RESULTS DIRECTORY PATH: " + results_directory)

    files = os.listdir(results_directory)

    print("FILES:")
    results = []
    for file in files:
        result = {}

        file_path = results_directory + "/" + file
        print(file_path)

        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                    if content.strip():
                        b64_content = base64.b64encode(content)
                        result["file_name"] = file
                        result["content_base64"] = b64_content.decode("UTF-8")
                        results.append(result)
                    else:
                        print("Empty File skipped: " + file_path)
            finally:
                f.close()
        else:
            print("Directory skipped: " + file_path)

    headers = {"Content-type": "application/json"}
    request_body = {"results": results}
    json_request_body = json.dumps(request_body)

    ssl_verification = True

    print("------------------CREATE PROJECT------------------")
    requests.post(
        allure_service_api_url + "/projects",
        headers=headers,
        json={"id": project_id},
        verify=ssl_verification,
    )

    print("------------------SEND-RESULTS------------------")
    response = requests.post(
        allure_service_api_url + "/send-results?project_id=" + project_id,
        headers=headers,
        data=json_request_body,
        verify=ssl_verification,
    )
    print("STATUS CODE:")
    print(response.status_code)
    print("RESPONSE:")
    json_response_body = json.loads(response.content)
    json_prettier_response_body = json.dumps(
        json_response_body, indent=4, sort_keys=True
    )
    print(json_prettier_response_body)


# Send results:
try:
    docker_allure_service_url = 'http://localhost:5050'
    results_dir = rf'{os.path.dirname(os.path.realpath(__file__))}\target\allure-results'

    # Send allure results with project_id in date format "yyyy-mm-dd":
    send_results(docker_allure_service_url, results_dir)

except Exception:
    print("Connection error occurred. Allure results have not been sent")
