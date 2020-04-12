# -*- coding: utf-8 -*-
from django.db import models
from addresses.models import Address
from reviews.models import Review
from stores.models import Store


class Mall(models.Model):
    name = models.CharField(max_length=100)
    trivia = models.TextField()
    is_working = models.BooleanField(default=False)
    stores = models.ManyToManyField(Store)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
