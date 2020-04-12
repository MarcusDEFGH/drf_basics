# -*- coding: utf-8 -*-
# Generated by Django 3.0.5 on 2020-04-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=2),
            preserve_default=False,
        ),
    ]
