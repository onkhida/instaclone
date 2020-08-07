from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# home page view for the application
@login_required # user must be logged in
def feed(request):
    posts = Post.objects.all() # all the posts

    context = {
        'posts': posts,
        'section': 'feed',
    }

    return render(request, 'posts/feed.html', context)

@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')

    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)

            if action == 'like':
                post.likes.add(request.user)
            else:
                post.likes.remove(request.user)
            return JsonResponse({'status': 'ok'})

        except:
            print('Something is wrong Danny!')

    return JsonResponse({'status': 'error'})
