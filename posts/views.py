from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# home page view for the application
def feed(request):
    posts = Post.objects.all() # all the posts

    context = {
        'posts': posts,
        'section': 'feed',
    }

    return render(request, 'posts/feed.html', context)
