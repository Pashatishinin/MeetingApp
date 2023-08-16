import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.forms import SelectDateWidget
from django.http import HttpResponse

from django.shortcuts import redirect, render, get_object_or_404

from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
            my_user = User.objects.create_user(user_name, email, password)
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.save()
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
            return redirect('meetings')
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
        meeting = form.save()
        MeetingHistory.objects.create(meeting=meeting, action='Added meeting')
        return super(MeetingCreate, self).form_valid(form)

    def get_initial(self):
        return {'user': self.request.user}


def create_view(request):
    pass
    # if request.method == 'POST':
    #     form = NewMeetingForm(request.POST)
    #     if form.is_valid():
    #         meeting = form.save()
    #         MeetingHistory.objects.create(meeting=meeting, action='Added meeting')
    #         return redirect('meetings')
    # else:
    #     form = NewMeetingForm(user=request.user.username)
    # return render(request, 'meetme/meeting_form.html', {"form": form})


def update_view(request, pk):
    obj = Meeting.objects.get(id=pk)
    if obj.user == request.user:
        if request.method == 'POST':
            form = NewMeetingForm(request.POST, instance=obj)
            if form.is_valid():
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


