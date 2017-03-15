from django.contrib.auth import get_user_model
from django.test import TestCase

from link.models import Link as DjangoLink

from jmbo_link. models import Link


class ViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(ViewsTestCase, cls).setUpTestData()

        # Editor
        cls.editor = get_user_model().objects.create(
            username="editor",
            email="editor@test.com",
            is_superuser=True,
            is_staff=True
        )
        cls.editor.set_password("password")
        cls.editor.save()

        # Create a test link
        obj, dc = Link.objects.get_or_create(
            title="Jmbo Link",
            owner=cls.editor,
            state="published",
            django_link=DjangoLink.objects.create(url="http://www.google.com")
        )
        obj.sites = [1]
        obj.save()
        cls.link = obj

    def test_detail(self):
        response = self.client.get(self.link.get_absolute_url())
        self.failUnless(self.link.title in response.content)
        self.failUnless(
            """<a href="http://www.google.com">""" in response.content
        )
