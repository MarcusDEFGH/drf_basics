# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path

from addresses.api.viewsets import AddressViewSet
from malls.api.viewsets import MallViewSet
from reviews.api.viewsets import ReviewViewSet
from stores.api.viewsets import StoreViewSet

from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'malls', MallViewSet, basename='Mall')
router.register(r'reviews', ReviewViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
