from django import views
from django.urls import path
from .views import UserCreateAPIView,UserListAPIView,UserRetriveAPIView,UserUpdateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',UserListAPIView.as_view()),
    path('<int:pk>/',UserRetriveAPIView.as_view()),
    path('<int:pk>/update/',UserUpdateAPIView.as_view()),
    path('sign-in/', TokenObtainPairView.as_view()),
    path('sign-in/refresh/', TokenRefreshView.as_view()),
    path('create/',UserCreateAPIView.as_view())
]

