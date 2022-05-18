from django.test import TestCase
from .models import User
from .serializers import UserSerializer
from rest_framework.test import APIRequestFactory
import json
from rest_framework import status
from rest_framework.test import force_authenticate
from .views import UserListAPIView

factory = APIRequestFactory()


class UserModelTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        User.objects.create_user(username="bakdaulet", password="123",
                                 email="bakosasdsah21345@gmail.com", phone="87059943864")

    def test_change_user_status(self):
        user = User.objects.get(username='bakdaulet')
        user.change_status('Online')
        self.assertEqual(
            user.status, "Online")


class GetAllUsersTest(TestCase):

    def setUp(self):
        User.objects.create_superuser(
            username="bakdaulet1", password="123", email="bakoasdassh21345@gmail.com", phone="87059943864")
        User.objects.create_user(username="bakdaulet2", password="123",
                                 email="baaasdassdkosh21345@gmail.com", phone="870599asd43864")
        User.objects.create_user(username="bakdaulet3", password="123",
                                 email="basdasakasdosh21345@gmail.com", phone="87059d943864")
        User.objects.create_user(username="bakdaulet4", password="123",
                                 email="basdasdaasdkosh21345@gmail.com", phone="870d59943864")

    def test_get_all_users(self):
        # get API response
        request = factory.get('/api/users/', format='json')
        user = User.objects.get(username='bakdaulet1')
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        view = UserListAPIView.as_view()
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

