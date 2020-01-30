from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'Project1/index.html')

def gettypes(request):
    type_list=Meeting.objects.all()
    return render(request, 'Project1/types.html' ,{'type_list' : type_list})