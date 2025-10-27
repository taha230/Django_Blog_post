
from django.contrib import admin
from django.urls import path

from posts.views import index, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/' , index),
    path('home/', home),
]
