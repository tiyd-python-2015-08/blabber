# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_twitter_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_username',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('@\\w+', message='Twitter names must be composed of alphanumeric characters')], null=True, blank=True),
        ),
    ]
