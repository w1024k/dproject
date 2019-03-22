# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', db_index=True)),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', db_index=True)),
                ('supplier', models.IntegerField(default=1, verbose_name='\u8d26\u53f7\u6765\u6e90', choices=[(1, '\u5fae\u4fe1'), (2, '\u652f\u4ed8\u5b9d'), (3, '\u65b0\u6d6a'), (4, '\u5176\u4ed6')])),
                ('openid', models.CharField(max_length=128, verbose_name='\u7b2c\u4e09\u65b9\u7528\u6237ID')),
                ('ticket', models.CharField(default='', max_length=128, verbose_name='\u7528\u6237\u51ed\u636e')),
                ('nickname', models.CharField(default='', max_length=32, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u7b2c\u4e09\u65b9\u8d26\u53f7',
                'verbose_name_plural': '\u7b2c\u4e09\u65b9\u8d26\u53f7',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='\u5173\u8054User')),
                ('mobile', models.CharField(default='', max_length=11, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81', db_index=True)),
                ('wechat', models.CharField(default='', max_length=32, verbose_name='\u5fae\u4fe1', blank=True)),
                ('address', models.CharField(default='', max_length=64, verbose_name='\u5730\u5740', blank=True)),
                ('avatar_path', models.CharField(default=b'/static/images/avatar.jpg', max_length=128, verbose_name='\u5934\u50cf\u6587\u4ef6')),
                ('intro', models.TextField(default='', verbose_name='\u4e2a\u4eba\u7b80\u4ecb', blank=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6269\u5c55\u8868',
                'verbose_name_plural': '\u7528\u6237\u6269\u5c55\u8868',
            },
        ),
        migrations.AddField(
            model_name='openuser',
            name='user',
            field=models.ForeignKey(verbose_name='\u5173\u8054\u7684User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='openuser',
            index_together=set([('supplier', 'openid')]),
        ),
    ]
