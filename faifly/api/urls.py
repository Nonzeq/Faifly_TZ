from django.contrib import admin

from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
    path('client/workerList/', WorkerListView.as_view()),
    path('client/worker/', WorkerByid.as_view()),
    path('client/locationsList/', LocationListView.as_view()),
    path('worker/AppointmentList/', AppointmentListView.as_view()),
    path('client/userAppointment/', AppointmentUser.as_view()),
    path('client/AddAppointment/', AppointmentAddView.as_view()),
    path('client/DeleteAppointment/<int:pk>/', DeleteUserAppointment.as_view()),
    path('client/SchelduleList/', SchelduleListVeiw.as_view()),
    path('client/GetFreeAppointment/', GetFreeAppointment.as_view()),
    # path('client/GetFreeAppointment/', YourView.as_view()),
]