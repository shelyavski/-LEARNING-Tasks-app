from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4,)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    username = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username
