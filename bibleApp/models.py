from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    # Additional fields
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)



class Church(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def clean(self):
        if not self.email.endswith('.org'):
            raise ValidationError('Church email must be an official email ending with .org')


class Community(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(CustomUser, related_name='communities')
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_communities')

    # Other fields and methods

class Team(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lead = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lead_teams')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams')

    # Other fields and methods


