from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Profile
from .forms import UserForm
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)
            user.save()

            profile = Profile(
                user=user,
                favorite_color='blue',
            )
            profile.save()

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            return redirect('recent_statuses')
    else:
        form = UserForm()
    return render(request, 'registration/register.html',
                  {'form': form})


def user_logout(request):
    logout(request)

    return redirect('recent_statuses')
