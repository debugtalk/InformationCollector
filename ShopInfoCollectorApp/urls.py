#encoding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('ShopInfoCollectorApp.views',
    url(r'^1-basicinfo/$', 'record_basicinfo', name='record_basicinfo'),
    url(r'^2-macaddress/$', 'record_macaddress', name='record_macaddress'),
    url(r'^3-contactinfo/$', 'record_contactinfo', name='record_contactinfo'),
    url(r'^4-chainstoreinfo/$', 'record_chainstoreinfo', name='record_chainstoreinfo'),
    url(r'^final-verification/$', 'final_verification', name='final_verification'),
    url(r'^finished/$', 'record_successfully', name='record_successfully'),
)
