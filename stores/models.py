# -*- coding: utf-8 -*-
from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.TextField()

    def __str__(self):
        return self.name
