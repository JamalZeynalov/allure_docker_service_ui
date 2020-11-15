from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import cache_control, never_cache

from service_ui.logic.allure_service_app import AllureServiceApp
from service_ui.logic.bar_plots import generate_tests_history_plot
from service_ui.logic.projects_filtering import (get_all_daily_reports,
                                                 get_latest_daily,
                                                 get_report_path_if_exists)


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def daily(request, report_date: str):
    if len(latest_10_projects := get_latest_daily()):

        report_path = get_report_path_if_exists(report_date)

        return render(
            request,
            "service_ui/daily.html",
            {"projects": latest_10_projects, "report_path": report_path},
        )
    else:
        return render(
            request,
            "service_ui/daily.html",
            {"report_path": "service_ui/not_found.html"},
        )


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def home(request):
    """ Show daily page with the latest report
    """
    if len(latest_10_projects := get_latest_daily()):
        latest_report_date = str(latest_10_projects[-1])

        return HttpResponseRedirect(f"/daily/{latest_report_date}")
    else:
        return render(
            request, "service_ui/daily.html", {"report_path": "no-content.jpg"}
        )


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def all_reports(request):
    """ Show the page with links to all reports
    """
    daily_reports = get_all_daily_reports()
    return render(request, "service_ui/all_reports.html", {"projects": daily_reports})


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def history(request):
    """ GGenerate "Daily History" plot that is based on results of latest 10 reports
    """
    latest_10_daily_reports = get_latest_daily()
    plot_div = generate_tests_history_plot(latest_10_daily_reports)

    return render(request, "service_ui/trend_graph.html", {"plot_div": plot_div})


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def delete_reports(request):
    """ Show the page with links to all reports
    """
    daily_reports = get_all_daily_reports()
    return render(
        request, "service_ui/delete_reports.html", {"projects": daily_reports}
    )


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def delete_report(request, report_date: str):
    """ Delete project and return HTTP response
    """
    return AllureServiceApp().delete_project(report_date)
