# -*- coding: utf-8 -*-
"""drf_basics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

router = routers.DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'malls', MallViewSet, basename='Mall')
router.register(r'reviews', ReviewViewSet)
router.register(r'stores', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
