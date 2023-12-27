from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'Home- Authorization'
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