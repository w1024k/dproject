# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20180513_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='openuser',
            name='state',
            field=models.IntegerField(default=0, db_index=True, verbose_name='\u8bb0\u5f55\u72b6\u6001', choices=[(0, '\u6709\u6548'), (1, '\u4e34\u65f6\u8bb0\u5f55'), (9, '\u5220\u9664')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default='', max_length=11, verbose_name='\u7535\u8bdd\u53f7\u7801', db_index=True),
        ),
    ]
