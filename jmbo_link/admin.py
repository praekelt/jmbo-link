from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from jmbo_link.forms import JmboLinkAdminForm
from jmbo_link.models import JmboLink
from link.admin import LinkAdmin

class JmboLinkAdmin(LinkAdmin):
    form = JmboLinkAdminForm

admin.site.register(JmboLink, ModelBaseAdmin)
