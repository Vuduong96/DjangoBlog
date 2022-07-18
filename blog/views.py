from ast import keyword
from django.shortcuts import render
from .models import Snippet


def home(request):
    context = { 
        'snippets': Snippet.objects.all()# key string need to the same spelling as the one in 'home.html'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def stringToList(string):
    listRes = list(string.split(","))
    return listRes

