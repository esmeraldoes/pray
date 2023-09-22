from django.db import models
from bibleApp.models import CustomUser


class Church(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_churches')

    def __str__(self):
        return self.name
    

class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    members = models.ManyToManyField(CustomUser, related_name='communities_joined', blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    team_lead = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    # team_lead = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='teams_led')
    members = models.ManyToManyField(CustomUser, related_name='teams_joined', blank=True)

    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    church = models.ForeignKey(Church, on_delete=models.SET_NULL, null=True, blank=True)
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    is_admin = models.BooleanField(default=False)  


    class Meta:
        unique_together = ('user', 'church', 'community', 'team')
