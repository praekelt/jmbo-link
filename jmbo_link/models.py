from django.core.urlresolvers import reverse, NoReverseMatch
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from jmbo.models import ModelBase
from link.models import ViewParam


class JmboLink(ModelBase):
    """
    A link class, similar to django-link, but subclassed from ModelBase.

    Since multiple inheritance from concrete django model classes results in
    clashes on id, title and slug, we subclass ModelBase and add the extra
    fields.
    """
    view_name = models.CharField(
        max_length=256, blank=True, null=True,
        help_text="View name to which this link will redirect."
    )
    view_params = models.ManyToManyField(
        ViewParam, blank=True, null=True
    )
    target_content_type = models.ForeignKey(
        ContentType, blank=True, null=True,
        related_name="jmbo_link_target_content_type"
    )
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey("target_content_type", "target_object_id")
    url = models.CharField(
        max_length=256, blank=True, null=True,
        help_text="URL to which this link will redirect."
    )

    class Meta:
        verbose_name = "Jmbo Link"
        verbose_name_plural = "Jmbo Links"
        ordering = ["title"]

    @property
    def absolute_url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        """
        Returns URL to which link should redirect based on a reversed view
        name, category, target or explicitly provided URL.

        This is an exact copy of the django-link method.
        """
        if self.view_name:
            kwargs = dict(
                (param.key, param.value) for param in self.view_params.all()
            )
            try:
                return reverse(self.view_name, kwargs=kwargs)
            except NoReverseMatch:
                pass
        elif self.target:
            try:
                return self.target.get_absolute_url()
            except AttributeError:
                pass
        else:
            # Django can be served in a subdirectory. Transparently fix urls.
            if "://" in self.url:
                return self.url

            # Urls not starting with a slash probably do so with reason. Skip.
            if not self.url.startswith("/"):
                return self.url

            # Request is not available here so use reverse to determine root
            try:
                root = reverse("home")
            except NoReverseMatch:
                return self.url

            # /abc and /root/abc must be transformed into /root/abc
            if not self.url.startswith(root):
                return root.rstrip("/") + "/" + self.url.lstrip("/")

        return self.url
