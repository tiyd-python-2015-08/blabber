from django.shortcuts import render
from django.http import HttpResponse
from .models import Status

# Create your views here.


def all_statuses(request):
    statuses = Status.objects.all()
    status_strings = [str(status) for status in statuses]
    return HttpResponse('<br>'.join(status_strings))


def recent_statuses(request):
    statuses = Status.objects.order_by('-posted_at')[:20]
    status_strings = [str(status) for status in statuses]
    # return HttpResponse('<br>'.join(status_strings))
    return render(request,
                  'updates/statuses.html',
                  {'statuses': status_strings})
