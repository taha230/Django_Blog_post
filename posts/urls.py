from django.urls import path, include
from .views import PostListRestView, PostDetailRestView, PostListRestViewGenerics, PostDetailRestViewGenerics, \
    PostDetailRestViewGenericsFull, PostListRestViewGenericsFull, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PostViewSet, basename='posts')

urlpatterns = [
    # path('', PostListRestView.as_view()), # as_view() method recognize the type of requests (get, post , ...)
    # path('', PostListRestViewGenerics.as_view()), # as_view() method recognize the type of requests (get, post , ...)
    # path('', PostListRestViewGenericsFull.as_view()), # as_view() method recognize the type of requests (get, post , ...)
    # path('', PostViewSet.as_view({'get' : 'list', 'post': 'create'}) ),
    # path('<int:pk>/', PostDetailRestView.as_view()),
    # path('<int:pk>/', PostDetailRestViewGenerics.as_view()),
    # path('<int:pk>/', PostDetailRestViewGenericsFull.as_view()),
    # path('<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete' : 'destroy'}))
     path('', include(router.urls))
]