
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated

from api.models.appointment import Appointment
from api.models.location import Location
from api.models.schedule import Schedule
from api.models.worker import Worker
from api.serializers import (
    WorkerSerializer,
    LocationSerializer,
    ScheduleSerializer,
    AppointmentSerializer, AddAppointmentSerializer, AppointmentFreeTimeSerializer
)

from api.tools import getDay


class WorkerByid(generics.ListAPIView):
    serializer_class = WorkerSerializer
    def get_queryset(self):
        queryset = Worker.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(pk=id)
        return queryset


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
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        worker = self.request.query_params.get('worker')
        date = self.request.query_params.get('date')
        if worker is not None:
            queryset = queryset.filter(apointment_worker=worker)
        if worker and date is not None:
            queryset = queryset.filter(apointment_worker=worker, date=date)
        return queryset

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)


class SchelduleListVeiw(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        work_day = self.request.query_params.get('work_day')
        worker = self.request.query_params.get('worker')
        queryset = Schedule.objects.all()

        if worker and work_day is not None:
            work_day = work_day.upper()
            queryset = queryset.filter(worker=worker, work_day=work_day)
        return queryset



class AppointmentAddView(generics.CreateAPIView):
    serializer_class = AddAppointmentSerializer
    queryset = Appointment.objects.all()
    # permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(user=request.user)


class AppointmentUser(generics.ListAPIView):
    serializer_class = AppointmentSerializer


    def get_queryset(self):
        queryset = Appointment.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:
            queryset = queryset.filter(user=user)
            return queryset


class DeleteUserAppointment(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = (IsAuthenticated,)






class GetFreeAppointment(generics.ListAPIView):
    serializer_class = AppointmentFreeTimeSerializer

    def get_queryset(self):

        worker = self.request.query_params.get('worker')
        date = self.request.query_params.get('date')
        queryset = self.time_filter(worker,date)
        return queryset


    def time_filter(self, worker, date):
        data = {}
        queryset_appointment = Appointment.objects.filter(date=date, apointment_worker=worker)
        queryset_schedule = Schedule.objects.filter(worker=worker, work_day=getDay(date))
        if queryset_schedule and not queryset_appointment:
            data['time_range'] = [f'{queryset_schedule.first().time_start} {queryset_schedule.last().time_end}']
            return [data]
        if not queryset_appointment:
            data['time_range'] = [f"Worker don't work on {date}"]
            return [data]

        interwal = []

        for schedule_item in queryset_schedule:
            queryset_appointment_range = queryset_appointment.filter(
                apointment_end__range=(schedule_item.time_start, schedule_item.time_end)
            )
            state = queryset_appointment[0].apointment_end
            if queryset_appointment[0].apointment_start > schedule_item.time_start:
                state = schedule_item.time_start
            for appoint_item in queryset_appointment_range:
                if schedule_item.time_start < appoint_item.apointment_start < schedule_item.time_end:
                    if state != appoint_item.apointment_start:
                        interwal.append(f'{state} - {appoint_item.apointment_start}')
                        state = appoint_item.apointment_end
            if queryset_appointment_range:
                if queryset_appointment_range.last().apointment_end != schedule_item.time_end:
                    interwal += [f'{queryset_appointment_range.last().apointment_end} - {schedule_item.time_end}']
            else:
                interwal += [f'{schedule_item.time_start} - {schedule_item.time_end}']

        data['time_range'] = interwal
        return [data]


