# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-24 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0014_release_0_9_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='view_grade',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='learningmodule',
            name='check_prerequisite_passes',
            field=models.BooleanField(default=False),
        ),
    ]
