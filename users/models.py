from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4,)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to='static/images/profiles/',
                                      default='static/images/profiles/default_profile_image.jpeg', null=True, blank=True)

    def __str__(self):
        return self.user.username
