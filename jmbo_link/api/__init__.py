from rest_framework.serializers import ReadOnlyField, Serializer

from jmbo import api as jmbo_api

from jmbo_link.models import Link


class PropertiesMixin(Serializer):
    content = ReadOnlyField()

    class Meta:
        fields = ("content",)


class LinkSerializer(
    PropertiesMixin, jmbo_api.ModelBaseSerializer
    ):

    class Meta(jmbo_api.ModelBaseSerializer.Meta):
        model = Link


class LinkObjectsViewSet(jmbo_api.ModelBaseObjectsViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkPermittedViewSet(jmbo_api.ModelBasePermittedViewSet):
    queryset = Link.permitted.all()
    serializer_class = LinkSerializer


def register(router):
    return jmbo_api.register(
        router,
        (
            ("link-link-permitted", LinkPermittedViewSet),
            ("link-link", LinkObjectsViewSet)
        )
    )
