from email import message
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

from django.contrib import auth, messages

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
                messages.success(request, f'{username},You have Successfuly logged in')

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))


                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()



    context = {
        'title': 'Home- Authorization',
        'form':form,
    }

    return render(request, 'user/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username} You have successfuly registered')
           
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Registration',
        'form': form,
    }
    return render(request, 'user/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
            form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated")
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)


    context = {
        'title': 'Home - Cabinet',
        'form': form,
    }

    return render(request, 'user/profile.html', context)


def users_cart(request):
    return render(request, 'user/users_cart.html')


@login_required
def logout(request):
    messages.success(request, "You are logged out")
    auth.logout(request)
    return redirect(reverse('main:index'))