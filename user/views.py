from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            auth.login(request, user)
            if request.GET.get('next', None):
                return redirect(request.GET['next'])
            return redirect('home')
    else:
        if request.GET.get('next', None):
            return render(request, 'register.html', {'next': request.GET['next']})
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'User does not exist',
                           extra_tags='username-error')
            return redirect('login')
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if request.GET.get('next', None):
                    return redirect(request.GET['next'])
                return redirect('home')
            else:
                messages.error(request, 'Password Incorrect',
                               extra_tags='password-error')
                return redirect('login')

    else:
        if request.GET.get('next', None):
            return render(request, 'login.html', {'next': request.GET['next']})
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')



