# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-27 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190626_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beers',
            name='ibu',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
