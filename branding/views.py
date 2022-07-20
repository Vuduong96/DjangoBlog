from django.shortcuts import render
from .models import Branding, Keyword


def home(request):
    context = { 
        'brandings': Branding.objects.all(),# key string need to the same spelling as the one in 'home.html'
        'keywords': Keyword.objects.all()
    }
    return render(request, 'branding/home.html', context)

def about(request):
    return render(request, 'branding/about.html', {'title': 'About'})



