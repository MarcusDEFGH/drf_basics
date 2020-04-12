# -*- coding: utf-8 -*-
from django.db import models


class Mall(models.Model):
    name = models.CharField(max_length=100)
    trivia = models.TextField()
    is_working = models.BooleanField(default=False)

    def __str__(self):
        return self.name
