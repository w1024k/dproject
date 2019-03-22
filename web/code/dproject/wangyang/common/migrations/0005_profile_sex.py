# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20180522_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='\u6027\u522b', choices=[(1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3'), (0, b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
    ]
