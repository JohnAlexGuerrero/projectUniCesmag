from django.shortcuts import render, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from accounts.forms import SignUpForm, LoginForm
from django.contrib import messages


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Felicidades !! Se ha creado con exito tu usuario.')
            user = form.save()
            group = Group.objects.get(name='usuario')
            user.groups.add(group)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password =  form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'LoggedIn successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, "accounts/login.html", {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')