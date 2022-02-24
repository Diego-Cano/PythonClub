from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your tests here.

class MeetingTest(TestCase):
   def test_string(self):
       type=Meeting(meetingTitle ="test")
       self.assertEqual(str(type), type.meetingTitle)

   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
   def test_string(self):
       type=Resource(resourceName ="Python Tutorial by learnpython.org")
       self.assertEqual(str(type), type.resourceName)

   def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
   def test_string(self):
       type=Event(eventTitle ="Test")
       self.assertEqual(str(type), type.eventTitle)

   def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'event')

 

