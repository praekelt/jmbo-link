from django.conf.urls import url

from jmbo.views import ObjectList, ObjectDetail


urlpatterns = [
    url(
        r"^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="link-categorized-detail"
    ),
    url(
        r"^(?P<slug>[\w-]+)/$",
        ObjectDetail.as_view(),
        name="link-detail"
    ),
]
