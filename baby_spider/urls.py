from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^spider/new/', views.spider_new, name='spider_new'),
    url(r'^detail/', views.detail, name='detail'),
    url(r'^list_spider', views.list_spider, name='list_spider'),
    url(r'^list_extract', views.list_extract, name='list_extract')

]