# -*- coding: utf-8 -*-
from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=10)
    extra = models.CharField(max_length=100)

    def __str__(self):
        if self.extra:
            return ', '.join([self.street, self.number, self.extra, self.city])
        return ', '.join([self.street, self.number, self.city])
