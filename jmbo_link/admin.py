from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from jmbo_link.models import Link


admin.site.register(Link, ModelBaseAdmin)
