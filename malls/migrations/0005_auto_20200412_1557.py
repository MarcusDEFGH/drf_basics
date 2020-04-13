# -*- coding: utf-8 -*-
# Generated by Django 3.0.5 on 2020-04-12 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('malls', '0004_mall_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mall',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='addresses.Address'),
        ),
    ]
