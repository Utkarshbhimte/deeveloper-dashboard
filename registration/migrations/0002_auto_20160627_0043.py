# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='github',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]