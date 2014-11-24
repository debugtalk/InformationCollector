from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SalesNetworkManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^record/', include('ShopInfoCollectorApp.urls', namespace='ShopInfoCollectorApp'), name='ShopInfoCollectorApp'),
)

from SalesNetworkManager.settings import STATIC_PATH
urlpatterns += patterns('',
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':STATIC_PATH}),
)
