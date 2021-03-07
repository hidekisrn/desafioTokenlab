from django.contrib import admin
from scheduler.models import Event

class Events(admin.ModelAdmin):
    list_display = ['description','start_time', 'end_time', 'user']
    list_display_links = ['description','start_time', 'end_time', 'user']
    search_fields = ('description','user')

admin.site.register(Event, Events)
