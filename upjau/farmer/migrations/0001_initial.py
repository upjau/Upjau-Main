# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-04 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer_farmLand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('state', models.CharField(max_length=25)),
                ('district', models.CharField(max_length=50)),
                ('subDistrict', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('size', models.IntegerField()),
                ('soilType', models.CharField(max_length=50)),
                ('waterSystem', models.CharField(max_length=25)),
                ('purpose', models.CharField(max_length=8)),
            ],
        ),
    ]