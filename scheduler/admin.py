from django.contrib import admin
from scheduler.models import Scheduler

class Schedules(admin.ModelAdmin):
    list_display = ('id', 'event')
    list_display_links = ('id', 'event')
    search_fields = ('event',)

admin.site.register(Scheduler, Schedules)
