from django.db import models
from bibleApp.models import CustomUser

class Supervisor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    

class DailyDevotion(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    assigned_user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_devotions',)
    supervisor = models.ForeignKey(Supervisor, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_devotions',)
   
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description[:50]  # Display a truncated description in admin

    class Meta:
        verbose_name_plural = "Daily Devotions"



class UserPrayerSession(models.Model):
    daily_devotion = models.ForeignKey(DailyDevotion, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    voice_detected = models.BooleanField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.start_time}'

    class Meta:
        verbose_name_plural = "Prayer Sessions"


class PrayerRecord(models.Model):
    session = models.ForeignKey(UserPrayerSession, on_delete=models.CASCADE)
    prayer_duration = models.DurationField()
    voice_duration = models.DurationField()
    voice_detected = models.BooleanField()

    def __str__(self):
        return f'{self.session.user.username} - {self.session.start_time}'
    

