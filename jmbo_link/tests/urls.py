from django.conf.urls import url, include
from django.contrib import admin

from jmbo.views import ObjectDetail
from jmbo_link.tests.views import TestView


urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^link/1/$", TestView.as_view(), name="link-1"),
    url(r"^link/2/$", TestView.as_view(), name="link-2"),
    url(r'^jmbo-link/', include("jmbo_link.urls", namespace="jmbo_link"))
]
