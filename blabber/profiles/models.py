import re
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


def is_valid_twitter_name(value):
    if not re.match(r'@\w+', value):
        raise ValidationError('Invalid Twitter username - must start with @ and only contain alphanumeric characters')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    favorite_color = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    web_address = models.URLField(null=True, blank=True)
    twitter_username = models.CharField(max_length=16, null=True, blank=True,
                                        validators=[RegexValidator(r'@\w+', message='Twitter names must be composed of alphanumeric characters')])
