# -*- coding: utf-8 -*-
from rest_framework import serializers

from malls.models import Mall


class MallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mall
        fields = ('id', 'name', 'trivia', 'address')
