from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all() # key string need to the same spelling as the one in 'home.html' 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})