# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-07 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0017_auto_20171104_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='mark_attendance',
        ),
        migrations.AddField(
            model_name='school',
            name='principal',
            field=models.CharField(default=1, max_length=500),
        ),
    ]
