# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from addresses.models import Address
from stores.models import Store
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
        read_only_fields = ('reviews',)

    def create_stores(self, stores, mall):
        for _store in stores:
            store = Store.objects.create(**_store)
            store.save()
            mall.stores.add(store)

    def create_address(self, _address):
        address = Address.objects.create(**_address)
        address.save()
        return address

    def create(self, validated_data):
        address = self.create_address(validated_data.pop('address'))
        stores = validated_data.pop('stores')
        mall = Mall.objects.create(address=address, **validated_data)
        self.create_stores(stores, mall)

        return mall

    def get_full_about(self, obj):
        return f'{obj.name} - {obj.about}'
