# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions

from stores.models import Store
from stores.api.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'about', 'address__street',)
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
