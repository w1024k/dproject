# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20180522_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_path',
            field=models.CharField(default=b'/static/images/avatar.jpg', max_length=256, verbose_name='\u5934\u50cf\u6587\u4ef6'),
        ),
    ]
