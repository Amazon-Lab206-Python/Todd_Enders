# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171109_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.EmailField(max_length=255),
        ),
    ]
