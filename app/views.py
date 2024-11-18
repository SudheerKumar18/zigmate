from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import UserPreference
from .serializers import UserPreferenceSerializer

class UserPreferenceListCreateView(generics.ListCreateAPIView):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer

class UserPreferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NotificationLog, UserPreference
from .serializers import NotificationLogSerializer
from django.utils.timezone import now

class SendNotificationView(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get("userId")
        notification_type = data.get("type")
        channel = data.get("channel")
        
        user_pref = UserPreference.objects.filter(user_id=user_id).first()
        if not user_pref:
            return Response({"error": "User not found"}, status=404)

        log = NotificationLog.objects.create(
            user=user_pref,
            type=notification_type,
            channel=channel,
            status='sent',  # Simulate sending
            sent_at=now(),
        )
        return Response(NotificationLogSerializer(log).data)


