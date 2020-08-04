from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import never_cache, cache_control

from service_ui.utils.bar_plots import generate_tests_history_plot
from service_ui.utils.projects_filtering import get_latest_daily, get_all_daily_reports


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def daily(request, report_date: str):
    if len(latest_10_projects := get_latest_daily()):
        request.report_date = report_date

        return render(request, 'service_ui/daily.html', {'projects': latest_10_projects,
                                                         'report_url': report_date})
    else:
        return render(request, 'service_ui/not_found.html')


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def home(request):
    if len(latest_10_projects := get_latest_daily()):
        report_date = str(latest_10_projects[-1])
        return HttpResponseRedirect(f'/daily/{report_date}')
    else:
        return render(request, 'service_ui/not_found.html')


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def all_reports(request):
    daily_reports = get_all_daily_reports()
    return render(request, 'service_ui/all_reports.html', {'projects': daily_reports})


@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def history(request):
    latest_10_daily_reports = get_latest_daily()
    generate_tests_history_plot(latest_10_daily_reports)

    return render(request, 'service_ui/trend_graph.html')
