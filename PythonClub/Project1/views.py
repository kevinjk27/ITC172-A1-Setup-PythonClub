from django.shortcuts import render,get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm
from .forms import MeetingMinutesForm
from .forms import EventForm
from .forms import ResourceForm
from django.contrib.auth.decorators import login_required

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

def newmeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'Project1/newmeeting.html', {'form': form})

def newmeetingminutes(request):
     form=MeetingMinutesForm
     if request.method=='POST':
          form=MeetingMinutesForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingMinutesForm()
     else:
          form=MeetingMinutesForm()
     return render(request, 'Project1/newmeetingminutes.html', {'form': form})

def newevent(request):
     form=EventForm
     if request.method=='POST':
          form=EventForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=EventForm()
     else:
          form=EventForm()
     return render(request, 'Project1/newevent.html', {'form': form})

def newresource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'Project1/newresource.html', {'form': form})


def loginmessage(request):
    return render(request, 'Project1/loginmessage.html')

def logoutmessage(request):
    return render(request, 'Project1/logoutmessage.html')

@login_required
def newmeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'Project1/newmeeting.html', {'form': form})