# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True)),
                ('bio', models.TextField(blank=True)),
                ('profile_photo', models.TextField(blank=True)),
                ('photo_list', models.TextField(blank=True)),
                ('stopflag', models.BooleanField()),
            ],
        ),
    ]
