# -*- coding: utf-8 -*-
from django.db import models
from addresses.models import Address
from reviews.models import Review
from stores.models import Store


class Mall(models.Model):
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField()
    is_working = models.BooleanField(default=False)
    stores = models.ManyToManyField(Store)
    reviews = models.ManyToManyField(Review, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                null=True, blank=True)
    logo = models.ImageField(upload_to='malls', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def has_stores(self):
        if Store.objects.filter(mall=self):
            return True
        return False
