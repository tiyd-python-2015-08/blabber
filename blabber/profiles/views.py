from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Profile
from .forms import UserForm, ProfileForm
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


@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'GET':
        profile_form = ProfileForm(instance=profile)
    elif request.method == 'POST':
        profile_form = ProfileForm(instance=profile, data=request.POST)
        # profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile has been updated')

    return render(request, 'profiles/edit_profile.html', {'form': profile_form})
