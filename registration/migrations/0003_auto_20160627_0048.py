# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160627_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='github',
            field=models.CharField(max_length=50),
        ),
    ]
