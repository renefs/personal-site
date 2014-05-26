from django.conf.urls import patterns, include, url

from renefernandezcom.views import *
from captcha import urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'renefernandezcom.views.home', name='home'),
    url(r'^curriculum-vitae/', 'renefernandezcom.views.curriculum', name='curriculum'),
    # url(r'^blog/', include('blog.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
)
