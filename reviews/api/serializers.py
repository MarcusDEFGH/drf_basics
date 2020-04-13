# -*- coding: utf-8 -*-
from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'user', 'text', 'score')
