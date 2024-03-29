import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms

from django.contrib.auth.models import User
from django.db import IntegrityError

from django.shortcuts import redirect, render

from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView

from django.urls import reverse_lazy

from .models import Meeting, MeetingHistory

from .forms import NewMeetingForm, SearchForm


"""""""""""""""""""""""""""""""""
HOME PAGE
"""""""""""""""""""""""""""""""""


def home(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        id_number = form.cleaned_data.get('id_number')
        if id_number.isdigit():
            is_exist = Meeting.objects.filter(id=int(id_number)).exists()
            if is_exist:
                return redirect(f"/meetme/meeting/{id_number}")

            # if ID number is not exist, go to basic page
            else:
                return render(request, "meetme/home.html",
                              {"form": form, "info": id_number})
        else:
            return render(request, "meetme/home.html",
                          {"form": form, "not_number": id_number})

    return render(request, "meetme/home.html", {"form": form})


"""""""""""""""""""""""""""""""""
LOGIN PAGE
"""""""""""""""""""""""""""""""""


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomLoginView(LoginView):
    template_name = "meetme/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('meetings')


"""""""""""""""""""""""""""""""""
REGISTER PAGE
"""""""""""""""""""""""""""""""""


def register_page(request):
    if request.method == 'POST':

        try:
            user_name = request.POST.get('username')
            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if user_name:
                my_user = User.objects.create_user(user_name, email, password)
                my_user.first_name = first_name
                my_user.last_name = last_name
                my_user.save()
                user = authenticate(request, username=user_name, password=password)
                if user is not None:
                    login(request, user)
                return redirect('meetings')

            else:
                return redirect('register')

        except IntegrityError as e:
            return render(request, "meetme/register.html", {"info": e, "username" : user_name})

    return render(request, "meetme/register.html")


"""""""""""""""""""""""""""""""""
MEETINGS
"""""""""""""""""""""""""""""""""


class Meetings(LoginRequiredMixin, ListView):
    model = Meeting
    context_object_name = 'meetings'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meetings'] = context['meetings'].filter(user=self.request.user).order_by('start_date')
        sorted_dates = sorted(context['meetings'].filter(user=self.request.user), key=lambda
            obj: obj.end_date if obj.end_date > datetime.date.today() else datetime.date.max)
        context['sorted_meetings'] = sorted_dates
        context['count'] = context['meetings'].count()
        context['timenow'] = timezone.now()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['sorted_meetings'] = context['meetings'].filter(title__icontains=search_input)

        context['search_input'] = search_input
        return context


class MeetingDetail(DetailView):
    model = Meeting


class MeetingCreate(LoginRequiredMixin, CreateView):
    model = Meeting
    form_class = NewMeetingForm
    success_url = reverse_lazy('meetings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        field_s_data = form.cleaned_data.get('start_date')
        field_e_data = form.cleaned_data.get('end_date')
        today = datetime.date.today()

        if field_s_data and field_e_data:

            if field_e_data < today:
                form.add_error(None, "The end date of the event cannot be earlier than the current date")
                return self.form_invalid(form)

            elif field_e_data < field_s_data:
                form.add_error(None, "The end date of the event cannot be earlier than the start date")
                return self.form_invalid(form)

            else:
                meeting = form.save()
                MeetingHistory.objects.create(meeting=meeting, action='Added meeting')
                return super(MeetingCreate, self).form_valid(form)

        else:
            form.add_error(None, "You forgot to indicate the event dates")
            return self.form_invalid(form)

    def get_initial(self):
        return {'user': self.request.user}


def update_view(request, pk):
    obj = Meeting.objects.get(id=pk)

    if obj.user == request.user:

        if request.method == 'POST':
            form = NewMeetingForm(request.POST, instance=obj)

            if form.is_valid():
                field_s_data = form.cleaned_data.get('start_date')
                field_e_data = form.cleaned_data.get('end_date')
                today = datetime.date.today()

                if field_s_data and field_e_data:

                    if field_e_data < today:
                        form.add_error(None, "The end date of the event cannot be earlier than the current date")
                        return render(request, 'meetme/meeting_form.html', {'form': form})

                    elif field_e_data < field_s_data:
                        form.add_error(None, "The end date of the event cannot be earlier than the start date")
                        return render(request, 'meetme/meeting_form.html', {'form': form})

                else:
                    form.add_error(None, "You forgot to indicate the event dates")
                    return render(request, 'meetme/meeting_form.html', {'form': form})
                form.save()
                return redirect('meetings')

        else:
            form = NewMeetingForm(instance=obj)

    else:
        return redirect("error")

    return render(request, 'meetme/meeting_form.html', {'form': form})


class MeetingDelete(LoginRequiredMixin, DeleteView):
    model = Meeting
    context_object_name = 'meetings'
    success_url = reverse_lazy('meetings')


"""""""""""""""""""""""""""""""""
INFO PAGE
"""""""""""""""""""""""""""""""""


def info_view(request):
    return redirect('home')


