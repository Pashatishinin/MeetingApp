import random

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, User, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from core import settings
from django.db import models
from django import forms


class User(AbstractUser):
    account_type = models.IntegerField(null=True, blank=True)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     account_type = models.IntegerField()
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()





# class CustomUserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     account_type = models.CharField(max_length=20, blank=True)
#     email = models.EmailField(max_length=70, blank=True)
#
#
#     def __str__(self):
#         return self.user.username


# class Meeting(models.Model):
#     user = models.ForeignKey(CustomUserProfile, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     start_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True, default=False)
#     end_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True, default=False)
#     coffee_bar = models.BooleanField(default=False)
#     coffee_station = models.BooleanField(default=False)
#     restaurant = models.BooleanField(default=False)
#     kst_number = models.IntegerField()
#     number_of_quests = models.IntegerField(null=True, default=False)
#     description = models.TextField(max_length=300, null=True, blank=True)
#     recorded = models.BooleanField(default=False)
#
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering = ['start_date']

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


# -----------------------NEW       ----------------------





