from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):  # Creates a profile every time a user is created.
    if created:
        user = instance
        user_profile = Profile.objects.create(
            user=user
        )
