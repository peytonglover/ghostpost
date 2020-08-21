from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.forms import AddPostForm
from homepage.models import Post
from datetime import datetime
# Create your views here.

def index(request): 
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def upvoteview(request, post_id):
    posts = Post.objects.get(id=post_id)
    posts.upvote += 1
    posts.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvoteview(request, post_id):
    posts = Post.objects.get(id=post_id)
    posts.downvote += 1
    posts.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                content = data.get('content'),
                boast_roast = data.get('boast_roast'),
                upvote = 0,
                downvote = 0,
                date= datetime.now()
            )
            return HttpResponseRedirect(reverse(index))
    form = AddPostForm()
    return render(request, 'forms.html', {'form': form})


def boast(request):
    posts = Post.objects.filter(boast_roast=True)
    return render(request, 'index.html', {'posts': posts})

def roast(request):
    posts = Post.objects.filter(boast_roast=False)
    return render(request, 'index.html', {'posts': posts})

def sortbyvotes(request):
    sorted_posts = sorted(Post.objects.all(), key=Post.counter_of_votes, reverse=True)
    return render(request, 'index.html', {'posts': sorted_posts})