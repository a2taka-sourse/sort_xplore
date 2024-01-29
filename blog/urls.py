# coding: utf-8

from rest_framework import routers
from django.urls import re_path
from django.urls import path
from .views import UserViewSet, EntryViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)

urlpatterns = [
    path("<str:name>", views.index, name="index"),
    path("sr/", views.v1, name="view 1"),
]