# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-22 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0003_ourusers_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourusers',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='profile_pictures/'),
        ),
    ]
