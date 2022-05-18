from rest_framework_json_api.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id','phone','username','email','status','password')
        extra_kwargs = {'password': {'write_only': True}}


class UserStatusChangeSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id','status',)

        