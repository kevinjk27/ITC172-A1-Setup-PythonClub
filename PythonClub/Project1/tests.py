from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

from .views import index, getmeetings, getresources, getevents
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

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