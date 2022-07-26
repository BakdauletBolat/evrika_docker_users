from rest_framework_json_api.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','title','descriptions','user','status')


class PostStatusChangeSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'status',)

        