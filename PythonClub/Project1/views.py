from django.shortcuts import render,get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'Project1/index.html')

def getmeetings(request):
    type_list=Meeting.objects.all()
    return render(request, 'Project1/meetings.html' ,{'type_list' : type_list})

def getresources(request):
    type_list=Resource.objects.all()
    return render(request, 'Project1/resources.html' ,{'type_list' : type_list})

def getevents(request):
    type_list=Event.objects.all()
    return render(request, 'Project1/events.html', {'type_list' : type_list})

def eventsdetails(request, id):
    event=get_object_or_404(Event, pk=id)
    return render(request, 'Project1/eventdetails.html', {'event' : event}
    )