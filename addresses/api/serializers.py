# -*- coding: utf-8 -*-
from rest_framework import serializers

from addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'street', 'number')
