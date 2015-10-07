from django.shortcuts import render
from django.http import HttpResponse
from .models import Status, User

# Create your views here.


def all_statuses(request):
    statuses = Status.objects.all()
    status_strings = [str(status) for status in statuses]
    return HttpResponse('<br>'.join(status_strings))


def recent_statuses(request):
    statuses = Status.objects.order_by('-posted_at')[:20]
    # status_strings = [str(status) for status in statuses]
    # return HttpResponse('<br>'.join(status_strings))
    return render(request,
                  'updates/statuses.html',
                  {'statuses': statuses})


def show_user(request, user_id):
    user = User.objects.get(pk=user_id)
    statuses = user.status_set.all().order_by('-posted_at')

    return render(request,
                  'updates/user.html',
                  {'user': user,
                   'statuses': statuses})


def show_user_by_username(request, username):
    user_id = User.objects.get(username=username).id
    return show_user(request, user_id=user_id)
