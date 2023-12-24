from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':"Home",
        'content': 'People It\'s a shop',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True,
        }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('about page')