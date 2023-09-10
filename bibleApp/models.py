from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.db import models



# class CustomUser(AbstractUser):
#     age = models.PositiveIntegerField(null=True, blank=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     bio = models.TextField(blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=10)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
#     phone_number = models.CharField(max_length=20, null=True, blank=True)
#     is_church_member = models.BooleanField(default=False)
#     is_church_admin = models.BooleanField(default=False) 

#     def __str__(self):
#         return self.username
    

from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    is_church_member = models.BooleanField(default=False)
    is_church_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# UserProfile Model
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    # Add other profile-related fields here as needed

    def __str__(self):
        return self.user.username























































































# class Church(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


#     def clean(self):
#         if not self.email.endswith('.org'):
#             raise ValidationError('Church email must be an official email ending with .org')


# class Community(models.Model):
#     church = models.ForeignKey(Church, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     members = models.ManyToManyField(CustomUser, related_name='communities')
#     admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_communities')

#     # Other fields and methods

# class Team(models.Model):
#     community = models.ForeignKey(Community, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     lead = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lead_teams')
#     members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams')

#     # Other fields and methods



