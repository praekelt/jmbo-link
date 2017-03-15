from django.db import models

from django.utils.functional import cached_property

from jmbo.models import ModelBase
from simplemde.fields import SimpleMDEField

from link.models import Link as DjangoLink


class Link(ModelBase):
    autosave_fields = ("markdown",)

    django_link = models.OneToOneField(DjangoLink)
    markdown = SimpleMDEField(null=True, blank=True)

    @cached_property
    def content(self):
        if not self.markdown:
            return ""
        return markdown.markdown(self.markdown)
