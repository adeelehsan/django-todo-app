# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170612_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='log',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('inprogress', 'In Progress'), ('complete', 'Complete')], default=('inprogress', 'In Progress'), max_length=200, null=True),
        ),
    ]
