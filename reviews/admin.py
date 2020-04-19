# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Review
from .actions import is_spam
from .actions import not_spam


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'is_spam']
    actions = [is_spam, not_spam]


admin.site.register(Review, ReviewAdmin)
