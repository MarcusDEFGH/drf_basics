# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from malls.models import Mall
from malls.models import Manager
from .serializers import MallSerializer


class MallViewSet(viewsets.ModelViewSet):
    serializer_class = MallSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ('name', 'about', 'address__street',)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Mall.objects.filter(is_working=True)
        filter_args = ['id', 'name']
        query = {}

        for arg in filter_args:
            value = self.request.query_params.get(arg, None)
            if value is not None:
                query[arg] = value

        return queryset.filter(**query)

    def list(self, request, *args, **kwargs):
        return super(MallViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(MallViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(MallViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(MallViewSet, self).retrieve(request,
                                                 *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(MallViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(MallViewSet, self).partial_update(request,
                                                       *args, **kwargs)

    @action(methods=['post'], detail=True)
    def set_manager(self, request, id):
        manager = Manager.objects.get(id=request.data['manager_pk'])
        mall = Mall.objects.get(pk=id)
        mall.manager = manager
        mall.save()

        return HttpResponse('The manager was set successfuly.')
