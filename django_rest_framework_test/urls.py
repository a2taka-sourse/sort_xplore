"""
URL configuration for django_rest_framework_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


# coding: utf-8

from django.conf.urls import include
from django.urls import re_path
from django.urls import path
from django.contrib import admin
from blog.urls import router as blog_router

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # blog.urlsをincludeする
    re_path(r'^api/', include(blog_router.urls)),
    path('', include("blog.urls")),
    
]

