"""security URL Configuration

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
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from security.safe import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'security.safe.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    # 文章页面设置
    url(r'^articles/(?P<pageId>\d+)/$', views.article),
    # 子页面路由设置
    url(r'^(?P<pageGroup>\w+)/$', views.group),
    url(r'^(?P<pageGroup>\w+)/(?P<page>\d+)/$', views.group),
    url(r'^(?P<pageGroup>\w+)/(?P<tag>\w+)/$', views.group),
    url(r'^(?P<pageGroup>\w+)/(?P<tag>\w+)/(?P<page>\d+)/$', views.group),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
