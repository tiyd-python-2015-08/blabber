# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20151012_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='twitter_username',
            field=models.CharField(null=True, max_length=16, blank=True),
        ),
    ]
