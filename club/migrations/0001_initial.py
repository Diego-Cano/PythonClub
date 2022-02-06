# Generated by Django 4.0 on 2022-02-01 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTitle', models.CharField(max_length=255)),
                ('eventLocation', models.CharField(max_length=255)),
                ('eventDate', models.DateField()),
                ('eventTime', models.TimeField()),
                ('eventDescription', models.TextField()),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingTitle', models.CharField(max_length=255)),
                ('meetingDate', models.DateField()),
                ('meetingTime', models.TimeField()),
                ('meetingLocation', models.CharField(max_length=255)),
                ('meetingAgenda', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceName', models.CharField(max_length=255)),
                ('resourceType', models.TextField()),
                ('resourceURL', models.URLField()),
                ('resourceDate', models.DateField()),
                ('resourceDescription', models.TextField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutesText', models.TextField()),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meetingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.meeting')),
            ],
            options={
                'db_table': 'meetingminutes',
            },
        ),
    ]