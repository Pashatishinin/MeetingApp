from django import forms
from django.forms import SelectDateWidget
from .models import Meeting, User


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.Form):
    id_number = forms.CharField()


class NewMeetingForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}), required=False)
    use_profile_names = forms.BooleanField(required=False, initial=True, label="Use profile names")
    class Meta:
        model = Meeting
        fields = ['first_name', 'last_name', 'title', 'start_date', 'end_date', 'coffee_bar', 'coffee_station', 'restaurant',
                  'kst_number', 'number_of_quests', 'description', 'use_profile_names']
        widgets = {
            'start_date': SelectDateWidget(),
            'end_date': SelectDateWidget(),
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'account_type']



