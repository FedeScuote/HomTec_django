# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-19 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160219_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
    ]