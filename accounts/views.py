from django.shortcuts import render, redirect
from .forms import UserRegisterForm, userLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(request, 'add user', 'success')
            return redirect('home')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login user', 'success')
                return redirect('home')
            else:
                messages.success(request, ' user or password not', 'danger')
    else:
        form = userLoginForm()
    return render(request, 'login.html', context={'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'logout user', 'success')
    return redirect('home')
