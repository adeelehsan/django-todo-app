# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('can_view', 'can view all task'),)},
        ),
    ]