import datetime

from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from faker import Faker
import random


from django import forms
from django.forms import ModelForm, PasswordInput
from .models import Meeting


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.Form):
    id_number = forms.IntegerField()


class NewMeetingForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput(format='%d-%m-%Y'))
    end_date = forms.DateField(widget=DateInput(format='%d-%m-%Y'))
    class Meta:
        model = Meeting
        fields = ['title', 'start_date', 'end_date', 'coffee_bar', 'coffee_station', 'restaurant',
                  'kst_number', 'number_of_quests', 'description']
        widgets = {
            'start_date': DateInput,
            'end_date': DateInput}


class RegisterForm(forms.ModelForm):
    user = forms.CharField()
    first_name = forms.CharField()
    second_name = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = '__all__'




# class NewMeetingForm(ModelForm):
#     user = forms.CharField(max_length=100)
#     start_date = forms.DateField(widget=DateInput)
#     end_date = forms.DateField(widget=DateInput)
#     title = forms.CharField(max_length=100)
#     coffee_bar = forms.BooleanField(required=False)
#     coffee_station = forms.BooleanField(required=False)
#     restaurant = forms.BooleanField(required=False)
#     kst_number = forms.IntegerField()
#     number_of_quests = forms.IntegerField()
#     description = forms.Textarea()
#
#     class Meta:
#         model = Meeting
#         fields = '__all__'
#         widgets = {
#             'start_date': forms.DateInput(format="%d.%m.%Y",
#                                      attrs={
#                                          "class": "form-control",
#                                          "value": datetime.datetime.strftime(datetime.datetime.now(),
#                                                                              format="%d.%m.%Y"),
#                                          "type": "datetime",
#                                      }
#                                      ),
#             'end_date': forms.DateInput(format="%d.%m.%Y",
#                                      attrs={
#                                          "class": "form-control",
#                                          "value": datetime.datetime.strftime(datetime.datetime.now(),
#                                                                              format="%d.%m.%Y"),
#                                          "type": "datetime",
#                                      }
#                                      ),
#             'random_code': forms.HiddenInput()
#         }

