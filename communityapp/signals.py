from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Membership

@receiver(post_save, sender=Membership)
def update_user_church(sender, instance, created, **kwargs):
    if created:
        instance.user.church = instance.church
        instance.user.save()
