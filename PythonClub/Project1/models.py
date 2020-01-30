from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    MeetingTitle=models.CharField(max_length=255)
    MeetingDate=models.DateField()
    MeetingTime=models.TimeField()
    MeetingLocation=models.CharField(max_length=255)
    Agenda=models.TextField()

    def __str__(self):
        return self.MeetingTitle
    
    class Meta:
        db_table='Meeting'
        verbose_name_plural='Meetings'


class MeetingMinutes(models.Model):
    Meeting=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    Attendance=models.ManyToManyField(User)
    MinutesText=models.TextField()

    def __str__(self):
        return self.MinutesText
    
    class Meta:
        db_table='MeetingMinute'
        verbose_name_plural='MeetingMinutes'


class Resource(models.Model):
    ResourceName=models.CharField(max_length=255)
    ResourceURL=models.URLField(null=True, blank=True)
    ResourceType=models.CharField(max_length=256)
    DateEntered=models.DateField()
    UserID=models.ForeignKey(User, on_delete=models.CASCADE)
    Description=models.TextField()

    def __str__(self):
        return self.ResourceName
    
    class Meta:
        db_table='Resource'
        verbose_name_plural='Resources'


class Event(models.Model):
    EventTitle=models.CharField(max_length=255)
    Location=models.CharField(max_length=255)
    Date=models.DateField()
    Time=models.TimeField()
    Description=models.TextField()
    UserID=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.EventTitle
    
    class Meta:
        db_table='Event'
        verbose_name_plural='Events'