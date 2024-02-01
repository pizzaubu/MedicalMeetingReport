from django.shortcuts import render
from listviews.models import Report


def home(request):
    reports = Report.objects.all().filter(is_available=True)
    print(reports)

    context = {
        'reports': reports,
        #'reports': [],
    }
    return render(request, 'home.html', context)