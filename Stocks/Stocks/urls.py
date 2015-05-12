
from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stockPresenter.views.home', name='home'),
    # url(r'^stockPresenter/', include('stockPresenter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'Stocks.views.home'),
    url(r'^stock/$', 'Stocks.views.home'),
    url(r'^list/$', 'Stocks.views.listCompanys'),
    url(r'^pageSubmit/(.+)/(.+)$', 'Stocks.views.pageSubmit'),
    url(r'^compare/$', 'Stocks.views.compare'),
    url(r'^compareSubmit/(.+)/(.+)/(.+)$','Stocks.views.compareSubmit'),
)
