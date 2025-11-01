
from django.contrib import admin
from django.urls import path

from posts.views import index, home, post_list, post_detail, post_create, PostList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/' , index),
    path('home/', home),
    # path('posts/', post_list , name = "post_list"), # function-based view
    path('posts/', PostList.as_view()), # class_based view
    path('posts/<int:post_id>/', post_detail, name="post_detail"),
    path('posts/create/', post_create, name="post_create"),
]
