from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    favorite_color = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    web_address = models.URLField(null=True, blank=True)
