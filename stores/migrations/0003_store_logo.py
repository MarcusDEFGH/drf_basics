# -*- coding: utf-8 -*-
# Generated by Django 3.0.5 on 2020-04-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='stores'),
        ),
    ]
