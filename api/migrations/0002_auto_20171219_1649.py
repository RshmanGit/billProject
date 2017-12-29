# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-12-19 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawmaterialorder',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='rawmaterialorder',
            name='recieved',
        ),
        migrations.AddField(
            model_name='order',
            name='quant_delivered',
            field=models.IntegerField(default=0),
        ),
    ]