from django.shortcuts import render

from project_constants import PROJECT_NAME


def dashboard(request):
    report_url = f"http://localhost:5050/allure-docker-service/projects/{PROJECT_NAME}/reports/latest/index.html"
    return render(request, 'service_ui/dashboard.html', {'report_url': report_url})
