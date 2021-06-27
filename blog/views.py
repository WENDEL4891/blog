from django.shortcuts import render, redirect
from datetime import datetime
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    datetime_now = datetime.now().strftime("%d/%m/%Y")
    posts = Post.objects.order_by('-date_added')
    shorted_posts = [
        {
            'id': post.id,
            'title': post.title,
            'text': post.text[:350],
            'date_added': post.date_added
        } for post in posts
    ]
    context = {
        'shorted_posts': shorted_posts,
        'datetime_now': datetime_now
    }
    return render(request, 'blog/index.html', context)

def topics(request):
    return render(request, 'blog/topics.html')

def new_post(request):
    if (request.method != "POST"):
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('..')
    context = {'form': form}
    return render(request, 'blog/new_post.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)    
    return render(request, 'blog/post.html', {'post': post})

def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if (request.method != "POST"):
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('..')    
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/edit_post.html', context)