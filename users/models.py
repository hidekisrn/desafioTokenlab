from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #Using only default fields from AbstractUser

    def available_date(self, start_time, end_time, event_id=None):
        return not self.events.filter(Q(Q(start_time__lte=start_time) & Q(end_time__gte=start_time)) |
                            Q(Q(start_time__lte=end_time) & Q(end_time__gte=end_time))
        ).exclude(id=event_id).exists()
