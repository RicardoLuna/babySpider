from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.spider_list, name='spider_list'),
    url(r'^spider/new/$', views.spider_new, name='spider_new')
]