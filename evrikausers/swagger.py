from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
authentication_classes=[JWTAuthentication],
   info=openapi.Info(
      title="Server API",
      default_version='v2',
      description="Evrika users CRUD",
      contact=openapi.Contact(email="bakosh21345@gmail.com",name="Bakdaulet"),
      license=openapi.License(name="BSD License"),
      
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]