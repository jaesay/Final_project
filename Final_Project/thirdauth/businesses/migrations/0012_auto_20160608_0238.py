# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0011_auto_20160608_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='reservation',
            field=models.CharField(default='', max_length=50),
        ),
    ]