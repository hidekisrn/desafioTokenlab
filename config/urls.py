from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from scheduler.views import EventViewSet
from users.views import user_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/events/', EventViewSet.as_view(), name='events'),
    path('api/auth/', obtain_auth_token, name='api_auth'),
    path('api/register/', user_register, name='register'),
]
