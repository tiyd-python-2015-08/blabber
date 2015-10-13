from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Status, User, Favorite
from .forms import StatusForm

# Create your views here.


def all_statuses(request):
    statuses = Status.objects.all()
    status_strings = [str(status) for status in statuses]
    return HttpResponse('<br>'.join(status_strings))


def recent_statuses(request):
    if request.user.is_authenticated():
        statuses = Status.objects.filter(
            user__profile__in=request.user.profile.following.all())
        statuses = statuses.order_by('-posted_at')[:20]
    else:
        statuses = Status.objects.order_by('-posted_at')[:20]
    # status_strings = [str(status) for status in statuses]
    # return HttpResponse('<br>'.join(status_strings))

    # statuses = statuses.select_related('user')
    statuses = statuses.prefetch_related('user')

    return render(request,
                  'updates/statuses.html',
                  {'statuses': statuses})


def status_detail(request, status_id):
    status = get_object_or_404(Status, pk=status_id)

    return render(request, 'updates/status_detail.html', {'status': status})


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


@login_required
def add_favorite(request, status_id):
    status = get_object_or_404(Status, pk=status_id)
    if not status.favorite_set.filter(user=request.user).exists():
        status.favorite_set.create(user=request.user)
    return redirect('status_detail', status_id)


@login_required
def remove_favorite(request, status_id):
    status = get_object_or_404(Status, pk=status_id)
    status.favorite_set.filter(user=request.user).delete()
    return redirect('status_detail', status_id)
