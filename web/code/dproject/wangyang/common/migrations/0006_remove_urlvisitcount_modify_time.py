# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_profile_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlvisitcount',
            name='modify_time',
        ),
    ]
