# -*- coding: utf-8 -*-
def is_spam(modeladmin, request, queryset):
    queryset.update(is_spam=True)


def not_spam(modeladmin, request, queryset):
    queryset.update(is_spam=False)


is_spam.short_description = 'Classify as spam'
not_spam.short_description = 'Classify as not spam'
