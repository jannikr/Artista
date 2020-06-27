from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    instagram_handle = models.CharField(max_length=100, blank=True, null=True)
