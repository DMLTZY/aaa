# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aaa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mobile',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
