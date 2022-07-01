from rest_framework import serializers
from .models.appointment import Appointment
from .models.location import Location
from .models.schedule import Schedule
from .models.worker import Worker


class WorkerSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='work_location.nameLocation', read_only=True)
    class Meta:
        model = Worker
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


