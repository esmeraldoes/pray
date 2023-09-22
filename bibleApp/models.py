from django.db import models
from django.contrib.auth.models import AbstractUser



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
    # church = models.ForeignKey('communityapp.Church', on_delete=models.SET_NULL, null=True, blank=True)

    # # church = models.ForeignKey(Church, on_delete=models.SET_NULL, null=True, blank=True)

    # joined_communities = models.ManyToManyField('communityapp.Community', related_name='community_members', blank=True)
    # joined_teams = models.ManyToManyField('communityapp.Team', related_name='team_members', blank=True)



    def __str__(self):
        return self.username

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


    def __str__(self):
        return self.user.username


