# -*- coding: utf-8 -*-
from rest_framework import viewsets
# from rest_framework.decorators import action

from malls.models import Mall
from .serializers import MallSerializer


class MallViewSet(viewsets.ModelViewSet):
    serializer_class = MallSerializer

    def get_queryset(self):
        queryset = Mall.objects.filter(is_working=True)
        query_dict = {}
        query_dict['id'] = self.request.query_params.get('id', None)
        query_dict['name'] = self.request.query_params.get('name', None)

        query = {key: query_dict[key] for key in query_dict.keys()
                 if query_dict[key]}

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

    # @action(methods=['get'], detail=True)
    # def alert(self, request, pk=None):
    #     breakpoint()
    #     pass
