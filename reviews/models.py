# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=2, decimal_places=1)
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return ': '.join([self.user.first_name, self.text[10] + '...'])
