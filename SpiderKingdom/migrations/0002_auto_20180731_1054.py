# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpiderKingdom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='check',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='warning',
            field=models.IntegerField(default=True),
        ),
    ]
