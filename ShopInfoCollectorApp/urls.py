#encoding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('ShopInfoCollectorApp.views',
    url(r'^1-districinfo/$', 'record_districinfo', name='record_districinfo'),
    url(r'^2-basicinfo/$', 'record_basicinfo', name='record_basicinfo'),
    url(r'^3-macaddress/$', 'record_macaddress', name='record_macaddress'),
    url(r'^4-contactinfo/$', 'record_contactinfo', name='record_contactinfo'),
    url(r'^5-chainstoreinfo/$', 'record_chainstoreinfo', name='record_chainstoreinfo'),
    url(r'^6-verification/$', 'content_verification', name='content_verification'),
    url(r'^6-done/$', 'record_successfully', name='record_successfully'),
)
