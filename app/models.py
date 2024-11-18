from django.db import models

# Create your models here.


class UserPreference(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('never', 'Never'),
    ]

    user_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    marketing = models.BooleanField(default=True)
    newsletter = models.BooleanField(default=False)
    updates = models.BooleanField(default=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='weekly')
    email_channel = models.BooleanField(default=True)
    sms_channel = models.BooleanField(default=False)
    push_channel = models.BooleanField(default=True)
    timezone = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id
class NotificationLog(models.Model):
    TYPE_CHOICES = [
        ('marketing', 'Marketing'),
        ('newsletter', 'Newsletter'),
        ('updates', 'Updates'),
    ]

    CHANNEL_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('push', 'Push'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(UserPreference, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    channel = models.CharField(max_length=10, choices=CHANNEL_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    sent_at = models.DateTimeField(null=True, blank=True)
    failure_reason = models.TextField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.user.user_id} - {self.type}"

