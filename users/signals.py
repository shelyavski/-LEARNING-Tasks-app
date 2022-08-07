from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):  # Creates a profile every time a user is created.
    if created:
        user = instance
        user_profile = Profile.objects.create(
            user=user,
            username=user.username,
        )


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.username = profile.username
        user.first_name = profile.name
        user.email = profile.email
        user.save()


