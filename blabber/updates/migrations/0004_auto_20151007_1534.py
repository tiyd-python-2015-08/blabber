# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0003_auto_20151006_1902'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'status')]),
        ),
    ]
