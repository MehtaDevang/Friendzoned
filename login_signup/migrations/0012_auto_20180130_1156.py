# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-30 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0011_auto_20180130_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
    ]
