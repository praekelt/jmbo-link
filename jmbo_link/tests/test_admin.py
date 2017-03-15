from django.contrib.auth import get_user_model
from django.test import TestCase

from link.models import Link as DjangoLink

from jmbo_link. models import Link


class AdminTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(AdminTestCase, cls).setUpTestData()

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

    def setUp(self):
        super(AdminTestCase, self).setUp()
        self.client.logout()

    def test_admin_link(self):
        response = self.client.get("/admin/jmbo_link/link/add/")
        self.assertEqual(response.status_code, 302)

    def test_admin_add(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/jmbo_link/link/add/")
        self.assertEquals(response.status_code, 200)

    def test_admin_change(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/jmbo_link/link/%s/change/" % self.link.pk)
        self.assertEquals(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
        super(AdminTestCase, self).tearDown()

