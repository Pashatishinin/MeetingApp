from django.urls import path
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    # HOME PAGE
    path('', views.home, name="home"),


    path('error/', TemplateView.as_view(template_name="meetme/error_message.html"), name='error'),

    path('create/', views.info_view, name="info"),


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
    path('meeting-update/<int:pk>/', views.update_view, name="meeting-update"),
    path('meeting-delete/<int:pk>/', views.MeetingDelete.as_view(), name="meeting-delete"),

    # USERS VIEW
    path('users/', views.users_view, name="users"),
    path('delete/<int:id>', views.delete_view, name="delete")
    ]


