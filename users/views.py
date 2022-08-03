from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# TODO: Add sessions
# TODO: Add signals -> create profile when creating user


@login_required(login_url='login')
def profile(request):  # TODO: Add view and model
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'profile.html')


def login_view(request):  # TODO: Add view
    page = 'login'

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist! Try again.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect!')

    context = {
        'page': page,
    }
    return render(request, 'login.html')


def logout_view(request):  # TODO: Add view
    logout(request)
    messages.error(request, 'User was logged out successfully.')
    return redirect('login')


def register_user(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('ITS A POST')
        if form.is_valid():
            print('and its valid')
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account created!')  # TODO: Fix how it's displayed

            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, 'An error has occurred during registration!')

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'login.html', context)
