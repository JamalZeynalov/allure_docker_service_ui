from django.http import HttpResponseRedirect
from django.shortcuts import render

from service_ui.utils.projects_filtering import get_latest_daily, get_all_daily_reports


def daily(request, report_date: str):
    latest_10_projects = get_latest_daily()

    report_url = f"http://localhost:5050/allure-docker-service/projects/{report_date}/reports/latest/index.html"
    if len(latest_10_projects):
        return render(request, 'service_ui/daily.html', {'projects': latest_10_projects,
                                                         'report_url': report_url})
    else:
        return render(request, 'service_ui/not_found.html')


def dashboard(request):
    latest_10_projects = get_latest_daily()

    if len(latest_10_projects):
        report_date = str(latest_10_projects[-1])
        return HttpResponseRedirect(f'/daily/{report_date}')
    else:
        return render(request, 'service_ui/not_found.html')


def all_reports(request):
    daily_reports = get_all_daily_reports()
    return render(request, 'service_ui/all_reports.html', {'projects': daily_reports})
