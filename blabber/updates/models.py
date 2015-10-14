from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Status(models.Model):

    class Meta:
        verbose_name_plural = 'statuses'

    # id is automatic
    text = models.CharField(max_length=141)
    posted_at = models.DateTimeField()
    user = models.ForeignKey(User)

    favorited_users = models.ManyToManyField(User, through='Favorite', related_name='favorited_updates')

    def favorite_count(self):
        return self.favorite_set.count()

    # def favorited_users(self):
    #     return [favorite.user for favorite in self.favorite_set.all()]

    def __str__(self):
        return '@{}: {}'.format(self.user, self.text)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)

    class Meta:
        unique_together = ('user', 'status')

    def __str__(self):
        return '@{} <3 {}'.format(self.user, self.status)


def is_valid_twitter_name(value):
    if not re.match(r'@\w+', value):
        raise ValidationError('Invalid Twitter username - must start with @ and only contain alphanumeric characters')


class Profile(models.Model):
    user = models.OneToOneField(User)
    favorite_color = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    web_address = models.URLField(null=True, blank=True)
    twitter_username = models.CharField(max_length=16, null=True, blank=True,
                                        validators=[RegexValidator(r'@\w+', message='Twitter names must be composed of alphanumeric characters')])
    following = models.ManyToManyField('Profile', related_name='followers')

    def __str__(self):
        return str(self.user)
