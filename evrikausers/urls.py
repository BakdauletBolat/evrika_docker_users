from django.contrib import admin
from django.urls import path,include,re_path
from .views import custom404
from .swagger import urlpatterns as swag_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),

]

urlpatterns += swag_urls

handler404 = custom404