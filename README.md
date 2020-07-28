# Daily Allure Reports
This web application is created to assemble all asynchronously uploading allure-results in one report. 
<br>This report will not be divided by launches. Each next bunch of test results during the day will update the daily report. If a test failed and then passed during the same date then its result will overridden to the latest one ("passed").
<br>And at the end of a day you will see how many of your tests were passed/failed/broken/skipped.

If you have multiple Test Automation projects with different tests and you want to get their latest results in one report then this app will be helpful for you.
You can push all results to this app and use allure annotations `@allure.epic`, `@allure.feature`, `@allure.story` to organize your tests.

This application is based on ["allure-docker-service"](https://github.com/fescobar/allure-docker-service)  project.

## Dependencies:
You need to have following tools installed and set up on your machine:
* Docker client
* Git client
* python
* pip

## Installation with Docker:
#### 1. Create a new directory.
#### 2. Create following `docker-compose.yml` file in the created directory:
```.yaml
version: "3.8"

services:
  allure_docker_service_ui:
    image: jamalzeinalov/allure_docker_service_ui
    container_name: allure_docker_service_ui
    environment:
      ALLURE_SERVICE_CONTAINER: allure_docker_service
    ports:
      - "8000:8000"
    depends_on:
      - allure_docker_service
    networks:
      - app-net
    volumes:
      - ./target/allure-results:/code/target/allure-results
      - ./target/default-reports:/code/target/default-reports
      - ./target/projects:/code/target/projects

  allure_docker_service:
    image: frankescobar/allure-docker-service
    container_name: allure-service
    environment:
      CHECK_RESULTS_EVERY_SECONDS: 5
      KEEP_HISTORY: "FALSE"
    ports:
      - "5050:5050"
    volumes:
      - ./target/allure-results:/app/allure-results
      - ./target/default-reports:/app/default-reports
      - ./target/projects:/app/allure-docker-api/static/projects
    networks:
      - app-net

networks:
  app-net:
```
#### 2. Run `docker-compose up` command in the created directory:
Note: Accept all disc sharing requested by Docker! This is required to mount applications volumes.
(or use `docker-compose up -d` to run containers in detached mode)<br>
This command will create `target` folder. All results sent to the service will be mounted into this folder.

## Usage:
You can use ["allure-results-sample"](https://github.com/JamalZeynalov/allure-results-sample) project to try it out.
Follow the steps in its description to generate test results. 

In that project (and in this repository) you will find ["send_allure_results.py"](/examples/send_allure_results.py) file. This file contains python script to send allure results to the service.
More ways to send results you can find [here](https://github.com/fescobar/allure-docker-service#send-results-through-api). <br> But you have to modify them accordingly to send results with "project_id" in ISO 8601 date format (YYYY-MM-DD).

After some results are uploaded you can navigate to the application dashboard and check reports:<br>
[http://localhost:8000](http://localhost:8000)
<br>Note: The image "not content available" will be displayed until some results are uploaded.

The allure docker service swagger documentation is available at the following link:<br>
[http://localhost:5050/allure-docker-service/swagger](http://localhost:5050/allure-docker-service/swagger)

## Web Pages:
#### 1. Dashboard
On this page a user can navigate through up to 10 latest daily reports. By default a user is redirected to the latest daily report.
Also `Latest` button will always lead to the latest available report.

<img src="https://raw.githubusercontent.com/JamalZeynalov/allure_docker_service_ui/master/images/latest.png" width=1100 alt="Latest">

You can use these reports as usual. All allure report features are available.

<img src="https://raw.githubusercontent.com/JamalZeynalov/allure_docker_service_ui/master/images/navigation.png" width=1100 alt="navigation">


#### 2. All Reports
This page contains links to all available daily reports. The number of reports on this page is not limited.

<img src="https://raw.githubusercontent.com/JamalZeynalov/allure_docker_service_ui/master/images/all_reports.png" width=1100 alt="all_reports">

#### 2. Daily History
This page contains a graph with results of latest 10 daily reports

<img src="https://raw.githubusercontent.com/JamalZeynalov/allure_docker_service_ui/master/images/history.png" width=1100 alt="history">

