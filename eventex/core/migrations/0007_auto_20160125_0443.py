# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160125_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='start',
            field=models.TimeField(blank=True, null=True, verbose_name='início'),
        ),
    ]
