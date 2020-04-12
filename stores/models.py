# -*- coding: utf-8 -*-
from django.db import models
from reviews.models import Review


class Store(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.TextField()
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.name
