from django.test import TestCase
from django.test.client import Client
from django.contrib.sites.models import Site


from jmbo_link import models


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.link_data = {
            "title": "Link 1 Title",
            "slug": "link-1-title",
            "url": "/link-1/"
        }
        self.link = models.JmboLink.objects.create(**self.link_data)
        self.link.sites = Site.objects.all()
        self.link.likes_enabled = False
        self.link.comments_enabled = False
        self.link.publish()

    def test_detail(self):
        response = self.client.get("/jmbo-link/%s/" % self.link_data["slug"])
        self.assertContains(response, self.link_data["title"])
