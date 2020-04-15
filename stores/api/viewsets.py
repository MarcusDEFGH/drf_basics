# -*- coding: utf-8 -*-
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from stores.models import Store
from stores.api.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'about', 'address__street',)
