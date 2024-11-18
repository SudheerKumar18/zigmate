from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status

class UserPreferenceTests(APITestCase):
    def test_create_preference(self):
        data = {
            "user_id": "user123",
            "email": "user@example.com",
            "marketing": True,
            "newsletter": False,
            "updates": True,
            "frequency": "weekly",
            "email_channel": True,
            "sms_channel": False,
            "push_channel": True,
            "timezone": "America/New_York",
        }
        response = self.client.post('/api/preferences/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

