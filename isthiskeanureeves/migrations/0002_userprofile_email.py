# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isthiskeanureeves', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.URLField(blank=True),
        ),
    ]
