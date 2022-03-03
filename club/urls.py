from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('getresources/', views.getresources, name='resources'),
    path('getmeetingss/', views.getmeetings, name='meetings'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
]
