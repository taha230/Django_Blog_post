
from django.contrib import admin
from django.urls import path

from posts.views import index, home, post_list, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/' , index),
    path('home/', home),
    path('posts/', post_list , name = "post_list"),
    path('posts/<int:post_id>/', post_detail, name="post_detail"),
]
