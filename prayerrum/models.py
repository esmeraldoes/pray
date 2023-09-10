from django.db import models

# Create your models here.
# models.py

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class PrayerRoom(models.Model):
    name = models.CharField(max_length=255)
    participants = models.ManyToManyField(User, related_name='prayer_rooms', blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_of')

    def __str__(self):
        return self.name

class Prayer(models.Model):
    room = models.ForeignKey(PrayerRoom, on_delete=models.CASCADE, related_name='prayers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prayers')
    content = models.TextField()
    is_heard = models.BooleanField(default=False)
    is_muted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.room} - {self.timestamp}"


