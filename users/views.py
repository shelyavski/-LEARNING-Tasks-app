from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# TODO: Add sessions
# TODO: Add signals -> create profile when creating user


@login_required
def profile(request):  # TODO: Add view and model
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))


def login_view(request):  # TODO: Add view
    page = 'login'
    context = {
        'page': page,
    }
    return render(request, 'login.html')


def logout_view(request):  # TODO: Add view
    return render(request, 'logout.html')


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

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'login.html', context)
