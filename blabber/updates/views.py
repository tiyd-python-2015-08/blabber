from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Status, User
from .forms import StatusForm

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
                  {'blabuser': user,
                   'statuses': statuses})


def show_user_by_username(request, username):
    user_id = User.objects.get(username=username).id
    return show_user(request, user_id=user_id)


@login_required
def new_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.user = request.user
            status.posted_at = datetime.now()
            status.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Your status has been posted!")

            return redirect('recent_statuses')
    else:
        form = StatusForm()

    return render(request, 'updates/new.html', {'form': form})
