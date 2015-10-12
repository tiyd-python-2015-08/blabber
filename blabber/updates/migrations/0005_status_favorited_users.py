# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('updates', '0004_auto_20151007_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='favorited_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='updates.Favorite', related_name='favorited_updates'),
        ),
    ]
