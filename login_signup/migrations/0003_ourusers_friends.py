# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-22 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0002_auto_20180122_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourusers',
            name='friends',
            field=models.ManyToManyField(null=True, related_name='_ourusers_friends_+', to='login_signup.OurUsers'),
        ),
    ]
