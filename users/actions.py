from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer

def get_tokens_for_user(user: User):
    refresh = RefreshToken.for_user(user)

    return {
         'access': str(refresh.access_token),
        'refresh': str(refresh),
        'id': user.id
    }