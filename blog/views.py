from django.shortcuts import render

posts = [
    {
        'author':'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 1, 2022'

    },
    {
        'author':'Natcha',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'July 1, 2022'

    }
]


def home(request):
    context = {
        'posts': posts # key string need to the same spelling as the one in 'home.html' 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})