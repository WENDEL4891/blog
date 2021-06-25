from django.shortcuts import render
from datetime import datetime
from .models import Post

# Create your views here.
def index(request):
    datetime_now = datetime.now().strftime("%d/%m/%Y")
    posts = Post.objects.order_by('-date_added')
    context = {
        'posts': posts,
        'datetime_now': datetime_now
    }
    return render(request, 'blog/index.html', context)

def topics(request):
    return render(request, 'blog/topics.html')

def posts(request):
    return render(request, 'blog/posts.html')