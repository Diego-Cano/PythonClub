from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda

class Meeting(models.Model):
    meetingTitle = models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField(auto_now=False, auto_now_add=False)
    meetingLocation = models.CharField(max_length=255)
    meetingAgenda = models.CharField(max_length=255)


    def __str__(self):
        return self.meetingTitle
 
    class Meta:
        db_table='meeting'

# Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text

class MeetingMinutes(models.Model):
    meetingId=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutesText=models.TextField()

    def __str__(self):
        return self.minutestext
    
    class Meta:
        db_table='meetingminutes'

# Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description
class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.TextField()
    resourceURL=models.URLField()
    resourceDate=models.DateField()
    userId=models.ForeignKey(User, on_delete=models.CASCADE)
    resourceDescription=models.TextField()

    def __str__(self):
        return self.resourceName
    
    class Meta:
        db_table='resource'

# Event which will have fields for event title, location, date, time, description and the user id of the member that posted it

class Event(models.Model):
    eventTitle = models.CharField(max_length=255)
    eventLocation = models.CharField(max_length=255)
    eventDate=models.DateField()
    eventTime=models.TimeField(auto_now=False, auto_now_add=False)
    eventDescription=models.TextField()
    
    def currentUser(request):
        currentUser = request.user
        return current_user.id

    def __str__(self):
        return self.eventTitle
    
    class Meta:
        db_table='event'


