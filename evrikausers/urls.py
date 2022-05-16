from django.contrib import admin
from django.urls import path,include
from .views import custom404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls'))
]

handler404 = custom404