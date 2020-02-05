from django.contrib import admin

# Register your models here.
from .models import Meeting, Resource, MeetingMinutes, Event

admin.site.register(Meeting)
admin.site.register(Resource)
admin.site.register(MeetingMinutes)
admin.site.register(Event)