from django.contrib import admin

from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
    path('client/workerList/', WorkerListView.as_view()),
    path('client/locationsList/', LocationListView.as_view()),
    path('worker/AppointmentList/', AppointmentListView.as_view()),
    path('client/SchelduleList/', SchelduleListVeiw.as_view()),
]