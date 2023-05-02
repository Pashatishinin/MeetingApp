from django.urls import path
from .views import Meetings, MeetingDetail, MeetingCreate, MeetingUpdate, MeetingDelete,CustomLoginView, RegisterPage, home

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', home, name="home"),
    path('login/', CustomLoginView.as_view(), name ="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name ="logout"),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', Meetings.as_view(), name="index"),

    path('meeting/<int:pk>/', MeetingDetail.as_view(), name="meeting"),
    path('meeting-create/', MeetingCreate.as_view(), name="meeting-create"),
    path('meeting-update/<int:pk>/', MeetingUpdate.as_view(), name="meeting-update"),
    path('meeting-delete/<int:pk>/', MeetingDelete.as_view(), name="meeting-delete")

    ]