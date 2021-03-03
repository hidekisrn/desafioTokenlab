from rest_framework import viewsets
from scheduler.models import Scheduler
from scheduler.serializer import SchedulerSerializer

class SchedulersViewSet(viewsets.ModelViewSet):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer