# -*- coding: utf-8 -*-
from rest_framework import viewsets

from stores.models import Store
from stores.api.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
