# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-03 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='head',
            field=models.ImageField(default='xxx/default.png', upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_del',
            field=models.IntegerField(default=0),
        ),
    ]
