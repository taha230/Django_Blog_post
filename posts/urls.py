from django.urls import path
from .views import PostListRestView, PostDetailRestView

urlpatterns = [
    path('', PostListRestView.as_view()), # as_view() method recognize the type of requests (get, post , ...)
    path('<int:post_id>/', PostDetailRestView.as_view()),
    ]