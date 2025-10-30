from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from django.shortcuts import render
from .forms import  PostForm


def index (request):
    #body
    return HttpResponse('Welcome to Django')

def home (request):
    return HttpResponse('<h3>Welcome to Homepage of blog</h3>')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, "posts/post_list.html", context= context)

def post_detail(request, post_id):
    post = Post.objects.get(pk = post_id)
    comments = Comment.objects.filter(post = post)
    context = {'post' : post, 'comments' : comments}
    return render(request, "posts/post_detail.html", context= context)

def post_create(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(type(form.cleaned_data))
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/posts/")
    else:
        form = PostForm()
    return render(request , "/post/post_create.html", {"form" : form})
