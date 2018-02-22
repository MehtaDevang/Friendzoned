# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-23 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0008_auto_20180123_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_to', models.EmailField(max_length=50)),
                ('message', models.TextField(max_length=2000)),
                ('message_time', models.DateTimeField()),
                ('message_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_signup.OurUsers')),
            ],
        ),
    ]
