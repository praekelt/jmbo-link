from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client

from jmbo_link import models

class AdminTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        # Editor
        cls.editor = get_user_model().objects.create(
            username="editor",
            email="editor@test.com",
            is_superuser=True,
            is_staff=True
        )
        cls.editor.set_password("password")
        cls.editor.save()

        # Create a test jmbo_link
        obj, dc = models.JmboLink.objects.get_or_create(
                title="Jmbo Link",
                owner=cls.editor, state="published",
            )
        obj.sites = [1]
        obj.save()
        cls.link = obj

    def setUp(self):
        self.client.logout()

    def test_admin_link(self):
        # ensure the link add page can be reached
        response = self.client.get("/admin/jmbo_link/jmbolink/add/")
        self.assertEqual(response.status_code, 302)

    def test_admin_add(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/jmbo_link/jmbolink/add/")
        self.assertEquals(response.status_code, 200)

    def test_admin_change(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/jmbo_link/jmbolink/%s/change/" % self.link.pk)
        self.assertEquals(response.status_code, 200)

    def test_admin_relation(self):
        self.client.login(username="editor", password="password")
        response = self.client.get("/admin/jmbo_link/jmbolink/add/")
        self.failUnless("jmbo_link" in response.content)

    def tearDown(self):
        self.client.logout()

