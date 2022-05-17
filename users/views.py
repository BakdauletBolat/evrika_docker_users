from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView
from .models import User
from .serializers import UserSerializer, UserStatusChangeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from .actions import get_tokens_for_user


class UserCreateAPIView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = self.perform_create(serializer)
        print(user)
        data = get_tokens_for_user(user)

        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserListAPIView(ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetriveAPIView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserStatusChangeSerializer

    def update(self, request, *args, **kwargs):

        if request.data.get('status') == None:
            return Response({'error': 'You submitted incorrect data'})
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        prev_status = instance.status
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        message = f"Status changed from {prev_status} to {serializer.data['status']}"
        returnData = serializer.data
        returnData['status'] = message
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(returnData)

