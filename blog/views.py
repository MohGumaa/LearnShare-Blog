from django.shortcuts import render

posts = [
    {
        'author': 'Jumaa',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '25/01/2021',
    },
    {
        'author': 'Ahmed',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '27/01/2021',
    },
]

def index(request):
    context = {
        'title_page': 'Home',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def about(request):
    context = {
        'title_page': 'About'
    }
    return render(request, 'blog/about.html', context)
