from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry, ToDoList, Item
from .serializer import UserSerializer, EntrySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

def index(response,id):
    ls = ToDoList.objects.get(id=id)
    items = ls.item_set.get(id=id)
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" % ls.name, item.text)

def v1(request):
    return render(request, "blog/index.html")
