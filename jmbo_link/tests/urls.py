from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework_extras import discover

from jmbo_link import api as link_api


admin.autodiscover()

router = routers.SimpleRouter()
link_api.register(router)
discover(router)

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r'^api/(?P<version>(v1))/', include(router.urls)),
    url(r"^jmbo/", include("jmbo.urls", namespace="jmbo")),
    url(r"^jmbo-link/", include("jmbo_link.urls", namespace="jmbo_link")),
    url(r"^comments/", include("django_comments.urls")),
]
