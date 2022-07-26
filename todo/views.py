from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from todo.serializers import PostSerializer, PostStatusChangeSerializer
from users.actions import get_tokens_for_user
from .models import Post
from rest_framework.response import Response
from rest_framework import status

class PostCreateView(CreateAPIView):
    
    resource_name = 'PostCreateView'
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    permission_classes = [IsAdminUser,]
    
    def perform_create(self, serializer):
        return serializer.save()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.user = request.user
        serializer.is_valid(raise_exception=True)
        post = self.perform_create(serializer)
        post.user = request.user
        post.save()
        return Response(data=serializer.data)
    
class PostUpdateAPIView(UpdateAPIView):
    resource_name = 'PostUpdateAPIView'
    queryset = Post.objects.all()
    serializer_class = PostStatusChangeSerializer
    permission_classes = [IsAdminUser]
    lookup_field = None

    def get_object(self):
        
        obj = Post.objects.get(id=self.request.data.get('id'))

        return obj

    def update(self, request, *args, **kwargs):
        if request.data.get('status') == None:
            return Response({'error': 'You submitted incorrect data'})
        instance = self.get_object()
        prev_status = instance.status
        serializer = self.get_serializer(instance, data=request.data)
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
    
class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    
class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Успешно удалено"})
    
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]
    
