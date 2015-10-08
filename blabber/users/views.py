from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        # attempting to log in
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('all_statuses')
        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})

    return render(request,
                  'users/login.html',
                  {})
