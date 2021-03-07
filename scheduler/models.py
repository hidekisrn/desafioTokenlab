from django.db import models
from django.core.exceptions import ValidationError
from users.models import User

class Event(models.Model):
    description = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey('users.User', related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} - {self.user.username}'

    def save(self, *args, **kwargs):
        if not self.user.available_date(self.start_time, self.end_time, self.pk):
            raise ValidationError('busy time')
        super(Event, self).save(*args, **kwargs)