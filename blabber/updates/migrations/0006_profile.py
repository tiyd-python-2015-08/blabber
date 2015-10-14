# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('updates', '0005_status_favorited_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('favorite_color', models.CharField(max_length=50, null=True, blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
                ('web_address', models.URLField(null=True, blank=True)),
                ('twitter_username', models.CharField(max_length=16, null=True, validators=[django.core.validators.RegexValidator('@\\w+', message='Twitter names must be composed of alphanumeric characters')], blank=True)),
                ('following', models.ManyToManyField(to='updates.Profile', related_name='followers')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
