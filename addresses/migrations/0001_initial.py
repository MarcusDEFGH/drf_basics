# -*- coding: utf-8 -*-
# Generated by Django 3.0.5 on 2020-04-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=10)),
                ('extra', models.CharField(max_length=100)),
            ],
        ),
    ]