from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



from .models import Meeting

from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = "meetme/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterPage(FormView):
    template_name = 'meetme/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)



class Meetings(LoginRequiredMixin, ListView):
    model = Meeting
    context_object_name = 'meetings'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meetings'] = context['meetings'].filter(user=self.request.user)
        context['count'] = context['meetings'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['meetings'] = context['meetings'].filter(title__icontains=search_input)

        context['search_input'] = search_input
        return context


class MeetingDetail(LoginRequiredMixin, DetailView):
    model = Meeting


class MeetingCreate(LoginRequiredMixin, CreateView):
    model = Meeting
    fields = '__all__'
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(MeetingCreate, self.form_valid(form))


class MeetingUpdate(LoginRequiredMixin, UpdateView):
    model = Meeting
    fields = '__all__'
    success_url = reverse_lazy('index')


class MeetingDelete(LoginRequiredMixin, DeleteView):
    model = Meeting
    context_object_name = 'meetings'
    success_url = reverse_lazy('index')


def home(request):

    return render(request, "meetme/home.html")

