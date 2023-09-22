from django.db import models
from bibleApp.models import CustomUser

# from django.contrib.auth.models import User
from django.utils.timezone import timedelta


class PrayerTracker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    voice_start_time = models.DateTimeField(null=True, blank=True)
    voice_duration = models.DurationField(default=0)
    active = models.BooleanField(default=False)
    voice_duration = models.DurationField(default=timedelta(seconds=0))


    def __str__(self):
        return f"Prayer Session for {self.user.username}"



