from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Church(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_churches')
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='churches', blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    church = models.ForeignKey(Church, on_delete=models.CASCADE, related_name='communities')
    members = models.ManyToManyField(User, related_name='joined_communities', blank=True)

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='teams')
    team_lead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='led_teams')
    members = models.ManyToManyField(User, related_name='joined_teams', blank=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_team_lead = models.BooleanField(default=False)
