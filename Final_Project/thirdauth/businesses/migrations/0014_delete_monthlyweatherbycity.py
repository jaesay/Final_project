# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0013_business_explanation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthlyWeatherByCity',
        ),
    ]