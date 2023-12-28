from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm

from django.contrib import auth

# Create your views here.
def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()



    context = {
        'title': 'Home- Authorization',
        'form':form,
    }

    return render(request, 'user/login.html', context)

def registration(request):
    context = {
        'title': 'Home - Registration',
    }
    return render(request, 'user/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Cabinet',
    }

    return render(request, 'user/profile.html', context)

def logout(request):
    ...