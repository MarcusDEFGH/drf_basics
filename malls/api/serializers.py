# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from malls.models import Mall
from stores.api.serializers import StoreSerializer
from addresses.api.serializers import AddressSerializer


class MallSerializer(serializers.ModelSerializer):

    stores = StoreSerializer(many=True)
    address = AddressSerializer()
    full_about = SerializerMethodField()

    class Meta:
        model = Mall
        fields = ('id', 'name', 'about', 'address', 'is_working', 'logo',
                  'stores', 'full_about', 'has_stores')

    def get_full_about(self, obj):
        return f'{obj.name} - {obj.about}'
