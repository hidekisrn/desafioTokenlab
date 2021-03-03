from django.db import models

class Scheduler(models.Model):
    event = models.CharField(max_length=30)

    def __str__(self):
        return self.event