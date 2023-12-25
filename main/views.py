from django.http import HttpResponse
from django.shortcuts import render

from goods.models import *

# Create your views here.
def index(request):

   

    context = {
        'title':"Home - Main",
        'content': 'Furniture Shop',
        
        }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title':'About us',
        'content': 'About page',
        'text_on_page': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio reprehenderit facilis rem earum corporis omnis nostrum tempora eligendi sit hic.'
    }
    return render(request, 'main/about.html', context)