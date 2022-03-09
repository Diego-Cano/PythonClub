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

 class MeetingTypeForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

#Form tests
class MeetingType_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form=MeetingTypeForm(data={'meetingTitle': "party", 'meetingAgenda' : "something"})
        self.assertTrue(form.is_valid())

class New_Meeting_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=meetingTitle.objects.create(meetingTitle='Party')
        self.prod = Meeting.objects.create(meetingTitle='The Party', meetingDate='2022-04-02', meetingTime='2pm' user=self.test_user, meetingLocation='DownTown', meetingAgenda='Have a good Time!')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newMeeting/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newmeeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/newmeeting.html')
