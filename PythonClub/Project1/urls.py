from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('getresources/', views.getresources, name='resources'),
    path('getevents/', views.getevents, name='events'),
    path('eventsdetails/<int:id>', views.eventsdetails, name='eventdetails'),
    path('newmeeting', views.newmeeting, name='newmeeting'),
    path('newmeetingminutes', views.newmeetingminutes, name='newmeetingminutes'),
    path('newevent', views.newevent, name='newevent'),
    path('newresource', views.newresource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]