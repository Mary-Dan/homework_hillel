from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.CharField(max_length=10, blank=True, help_text='Enter your age:')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


