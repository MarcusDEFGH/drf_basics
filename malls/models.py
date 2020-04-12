# -*- coding: utf-8 -*-
from django.db import models
from stores.models import Store
from reviews.models import Review


class Mall(models.Model):
    name = models.CharField(max_length=100)
    trivia = models.TextField()
    is_working = models.BooleanField(default=False)
    stores = models.ManyToManyField(Store)
    reviews = models.ManyToManyField(Review)

    def __str__(self):
        return self.name
