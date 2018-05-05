# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u65e5\u671f', db_index=True)),
                ('count', models.IntegerField(default=0, verbose_name='\u603b\u6570')),
                ('event', models.PositiveSmallIntegerField(db_index=True, verbose_name='\u7edf\u8ba1\u4e8b\u4ef6\u7c7b\u578b', choices=[(1, '\u7f51\u7ad9\u603b\u8bbf\u95ee\u6570')])),
            ],
            options={
                'verbose_name': '\u6bcf\u65e5\u6570\u636e\u7edf\u8ba1',
                'verbose_name_plural': '\u6bcf\u65e5\u6570\u636e\u7edf\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='UrlVisitCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', db_index=True)),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', db_index=True)),
                ('client_ip', models.GenericIPAddressField(default=b'0.0.0.0', verbose_name='\u5ba2\u6237\u7aefIP')),
                ('url', models.CharField(default=b'/wangyang/', max_length=128, verbose_name='\u94fe\u63a5\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u94fe\u63a5\u8bbf\u95ee\u6570\u636e\u7edf\u8ba1',
                'verbose_name_plural': '\u94fe\u63a5\u8bbf\u95ee\u6570\u636e\u7edf\u8ba1',
            },
        ),
    ]
