# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 03:00
from __future__ import unicode_literals

import day06.tools
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day06', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='head',
            field=models.FileField(storage=day06.tools.ImageStorage(), upload_to='account/user/zhangsan/%Y%m%d'),
        ),
    ]
