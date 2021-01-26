from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        'title_page': 'Home',
        'posts': Post.objects.all().order_by('-date_posted'),
    }
    return render(request, 'blog/index.html', context)

def about(request):
    context = {
        'title_page': 'About'
    }
    return render(request, 'blog/about.html', context)
