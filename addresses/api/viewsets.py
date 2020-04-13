# -*- coding: utf-8 -*-
from rest_framework import viewsets

from addresses.models import Address
from addresses.api.serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
