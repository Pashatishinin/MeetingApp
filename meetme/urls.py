from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    # HOME PAGE
    path('', views.home, name="home"),

    # LOGIN/LOGOUT/REGISTER
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', views.register_page, name='register'),

    # MEETING LIST PAGE
    path('meetings/', views.Meetings.as_view(), name="meetings"),

    # MEETING DETAIL
    path('meeting/<int:pk>/', views.MeetingDetail.as_view(), name="meeting"),

    # MEETING CREATE/UPDATE/DELETE
    path('meeting-create/', views.MeetingCreate.as_view(), name="meeting-create"),
    path('meeting-update/<int:pk>/', views.MeetingUpdate.as_view(), name="meeting-update"),
    path('meeting-delete/<int:pk>/', views.MeetingDelete.as_view(), name="meeting-delete")
    ]
