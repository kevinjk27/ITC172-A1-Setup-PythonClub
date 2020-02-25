from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

from .views import index, getmeetings, getresources, getevents
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import MeetingForm, MeetingMinutesForm, EventForm, ResourceForm

# Create your tests here.

# TESTING models
class MeetingTest(TestCase):
   def setUp(self):
       self.meeting = Meeting(MeetingTitle="How to be Better Employer 101",
       MeetingDate="2020-02-29",
       MeetingTime="18:00:00",
       MeetingLocation="300 Banana St",
       Agenda="How to be Better Employer 101 will invite Forbes Top 30 hiring manager"
       )

   def test_table(self):
       self.assertEqual(str(self.meeting._meta.db_table), 'Meeting')


   def test_string(self):
       self.assertEqual(str(self.meeting), self.meeting.MeetingTitle)

   def test_meeting_date(self):
       self.assertEqual(self.meeting.MeetingDate, "2020-02-29")

   def test_meeting_time(self):
       self.assertEqual(self.meeting.MeetingTime, "18:00:00")

   def test_meeting_location(self):
       self.assertEqual(self.meeting.MeetingLocation, "300 Banana St")

   def test_meeting_agenda(self):
       self.assertEqual(self.meeting.Agenda, "How to be Better Employer 101 will invite Forbes Top 30 hiring manager")

# TESTING views
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
  
class GetMeetingsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('meetings'))
       self.assertEqual(response.status_code, 200)

class GetResourcesTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('resources'))
       self.assertEqual(response.status_code, 200)

class GetEventsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('events'))
       self.assertEqual(response.status_code, 200)



class GetEventDetailsTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username="Kevin", password="1234")
        self.event=Event.objects.create(
            EventTitle='Book Fair 2020',
            Location='Lima Hall',
            Date='2020-01-30',
            Time='18:00:00',
            Description='Book Fair 2020 is the biggest book fair in WA State.',
            UserID=self.user)

    def test_event_detail_success(self):
        response = self.client.get(reverse('eventdetails', args=(self.event.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)


# TESTING forms
class Meeting_Form_Test(TestCase):
    def test_meeting_form_is_valid(self):
        form=MeetingForm(data={'MeetingTitle': "Board of Chamber",
        'MeetingDate' : "2020-05-12",
        'MeetingTime' : "14:00:00",
        'MeetingLocation' : "S Jackson St",
        'Agenda' : "Selecting a new leader"})
        self.assertTrue(form.is_valid())

    def test_meeting_form_empty(self):
        form=MeetingForm(data={'MeetingTitle': ""})
        self.assertFalse(form.is_valid())



class ResourceForm_Form_Test(TestCase):
    def test_resource_user_foreign_key(self):
        self.user = User.objects.create(username='new user', password='pass')



    def test_resource_form_is_valid(self):
        form=ResourceForm(data={'ResourceName' : "Database Design for Mere Mortals",
        'ResourceURL' : "https://www.bookfinder.com/buyback/search/#9780321884497",
        'ResourceType' : "Textbook",
        'DateEntered' : "2020-01-30",
        'UserID' : "user",
        'Description' : "A Hands-On Guide to Relational Database Design"})


    def test_resource_form_empty(self):
        form=ResourceForm(data={'ResourceName': ""})
        self.assertFalse(form.is_valid())