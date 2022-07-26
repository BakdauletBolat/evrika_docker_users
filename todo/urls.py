from django import views
from django.urls import path

from todo.views import PostCreateView, PostDestroyAPIView, PostListAPIView, PostRetrieveAPIView, PostUpdateAPIView


urlpatterns = [
    path('',PostListAPIView.as_view()),
    path('<int:pk>/',PostRetrieveAPIView.as_view()),
    path('update/',PostUpdateAPIView.as_view()),
    path('delete/<int:pk>/', PostDestroyAPIView.as_view()),
    path('create/',PostCreateView.as_view())
]

