from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import  PostForm
from django.views import generic


def index (request):
    #body
    return HttpResponse('Welcome to Django')

def home (request):
    return HttpResponse('<h3>Welcome to Homepage of blog</h3>')

def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, "posts/post_list.html", context= context)

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "posts/post_list.html"
    context_object_name = 'posts'

def post_detail(request, post_id):
    # try:
    #     post = Post.objects.get(pk = post_id)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound('Post does not exists !!!')

    post = get_object_or_404(Post, pk=post_id)

    comments = Comment.objects.filter(post = post)
    context = {'post' : post, 'comments' : comments}
    return render(request, "posts/post_detail.html", context= context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    # context_object_name = 'post'

    # def get_queryset(self, post_id):
    #     return get_object_or_404(Post, pk=self.request.POST['post_id'])

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        print(kwargs) # for print the value of kwargs
        context['comments'] = Comment.objects.filter(post = kwargs['object'].pk)
        return context


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
    return render(request , "posts/post_create.html", {"form" : form})
