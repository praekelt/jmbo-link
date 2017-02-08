from jmbo import api as jmbo_api

from jmbo_link.models import JmboLink


class JmboLinkObjectsViewSet(jmbo_api.ModelBaseObjectsViewSet):
    queryset = JmboLink.objects.all()


class JmboLinkPermittedViewSet(jmbo_api.ModelBasePermittedViewSet):
    queryset = JmboLink.permitted.all()


def register(router):
    router.register(
        r"jmbo_link-jmbolink",
        JmboLinkObjectsViewSet,
    )
    router.register(
        r"jmbo_link-jmbolink-permitted",
        JmboLinkPermittedViewSet,
    )
