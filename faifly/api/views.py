from rest_framework import generics
from api.models.appointment import Appointment
from api.models.location import Location
from api.models.schedule import Schedule
from api.models.worker import Worker
from api.serializers import (
                                WorkerSerializer,
                                LocationSerializer,
                                ScheduleSerializer,
                                AppointmentSerializer
                            )


from api.tools import getDay


class WorkerListView(generics.ListCreateAPIView):

    serializer_class = WorkerSerializer

    def get_queryset(self):
        queryset = Worker.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(work_location=location)
        return queryset


class LocationListView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class AppointmentListView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        worker = self.request.query_params.get('worker')
        date = self.request.query_params.get('date')
        if worker and date is not None:
            queryset = queryset.filter(apointment_worker=worker,date=date)
        return queryset

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)


class SchelduleListVeiw(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        work_day = self.request.query_params.get('work_day')
        work_day = getDay(work_day)
        worker = self.request.query_params.get('worker')
        queryset = Schedule.objects.all()

        if worker is not None:
            queryset = queryset.filter(worker=worker, work_day=work_day)
        return queryset













