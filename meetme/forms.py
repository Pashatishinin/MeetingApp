import datetime

from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from faker import Faker
import random


from django import forms
from django.forms import ModelForm, PasswordInput, SelectDateWidget
from .models import Meeting


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.Form):
    id_number = forms.CharField()


class NewMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'start_date', 'end_date', 'coffee_bar', 'coffee_station', 'restaurant',
                  'kst_number', 'number_of_quests', 'description']
        widgets = {
            'start_date': SelectDateWidget(),
            'end_date': SelectDateWidget(),
        }



class RegisterForm(forms.ModelForm):
    user = forms.CharField(required=False)
    first_name = forms.CharField()
    second_name = forms.CharField()
    user_type = forms.NumberInput()
    password = forms.CharField(required=False)
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = '__all__'





