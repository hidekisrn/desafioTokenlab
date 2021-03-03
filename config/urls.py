from django.contrib import admin
from django.urls import path, include
from scheduler.views import SchedulersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'schedulers', SchedulersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
