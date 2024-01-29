from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry, Class, Item
from .serializer import UserSerializer, EntrySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

def index(response,id):
    ls = Class.objects.get(id=id)
    items = ls.item_set.get(id=id)
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" % ls.name, item.text)

def v1(request):
    return render(request, "blog/index.html")

class IndexView(View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.all()
        return render(request, 'app/index.html', {
            'blog_data': blog_data,
        })


class AddView(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('number')

        blog = Blog()
        blog.title = title
        blog.save()

        data = {
            'title': title,
        }
        return JsonResponse(data)


class SearchView(View):
    def post(self, request, *args, **kwargs):
        title = request.POST.get('number')
        blog_data = Blog.objects.all()
        title_list = []

        if title:
            blog_data = blog_data.filter(title__icontains=title)

        for blog in blog_data:
            title_list.append(blog.title)

        data = {
            'title_list': title_list,
        }
        return JsonResponse(data)