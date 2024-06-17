
from django.contrib.auth.models import AbstractUser

from core import settings
from django.db import models


class User(AbstractUser):
    account_type = models.IntegerField(null=True, blank=True)


class Meeting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True, default=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True, default=False)
    coffee_bar = models.BooleanField(default=False)
    coffee_station = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    kst_number = models.IntegerField()
    number_of_quests = models.IntegerField(null=True, default=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    recorded = models.BooleanField(default=False)


class MeetingHistory(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='history')
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_value = models.TextField(blank=True)
    new_value = models.TextField(blank=True)

    def __str__(self):
        return f'{self.meeting} - {self.action}'







