from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from termcolor import colored
from .forms import  PostForm
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer

from rest_framework.views import APIView
from django.http import Http404

class PostListRestView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListRestViewGenericsFull( generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListRestViewGenerics(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, ** kwargs):
        return self.list(request, *args, ** kwargs)
    def post(self, request, *args, ** kwargs):
        return self.create(request, *args, ** kwargs)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['GET', 'POST'])
def index (request):
    #body
    # return HttpResponse('Welcome to Django')
    pk = request.query_params.get('pk')

    print(request.query_params)
    try:
        p = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'msg' : 'Post Does not Exists !!!' , 'status' : status.HTTP_404_NOT_FOUND})
    serializer = PostSerializer(p)
    print(serializer)
    print('-' * 100)
    # print(request.data)
    print(serializer.data)

    # return Response({'msg' :'Hello Django from REST Framework'})
    return Response(serializer.data )

def home (request):
    return HttpResponse('<h3>Welcome to Homepage of blog</h3>')


# function-based view
def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, "posts/post_list.html", context= context)

# class-based view
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "posts/post_list.html"
    context_object_name = 'posts'

# function-based view
def post_detail(request, post_id):
    # try:
    #     post = Post.objects.get(pk = post_id)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound('Post does not exists !!!')

    post = get_object_or_404(Post, pk=post_id)

    comments = Comment.objects.filter(post = post)
    context = {'post' : post, 'comments' : comments}
    return render(request, "posts/post_detail.html", context= context)

class PostDetailRestView(APIView):
    def get_object(self, pk):
        try:
            post = Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            raise Http404
        return post

    def get(self, request , pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request , pk):
        post = self.get_object(pk)

        serializer = PostSerializer(post, data= request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostDetailRestViewGenericsFull(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailRestViewGenerics(mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, ** kwargs):
        return self.retrieve(request, *args, ** kwargs)
    def put(self, request, *args, ** kwargs):
        return self.update(request, *args, ** kwargs)
    def delete(self, request, *args, ** kwargs):
        return self.destroy(request, *args, ** kwargs)

# class-based view
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

# with form
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
