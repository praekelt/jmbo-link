from django.conf.urls import url

from jmbo.views import ObjectList, ObjectDetail


urlpatterns = [
    url(
        r"^(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="jmbo-link-detail"
    ),
]
