"""blabber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import updates.views as views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^statuses/all', views.all_statuses),
    url(r'^statuses/', views.recent_statuses),
    url(r'^user/(?P<user_id>\d+)$', views.show_user),
    url(r'^user/(?P<username>\S+)$', views.show_user_by_username),
]
