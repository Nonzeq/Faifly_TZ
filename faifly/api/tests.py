from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ScheduleTests(APITestCase):


    def test_create_shedule(self):
        data = {"worker": 1, "work_day": "MONDAY", "time_start": "13:00", "time_end": "15:00", "work_location": 1}
        response = self.client.post('/api/client/AddAppointment/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
