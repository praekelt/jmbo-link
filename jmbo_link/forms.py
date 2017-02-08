from link.forms import LinkAdminForm
from jmbo_link.models import JmboLink

class JmboLinkAdminForm(LinkAdminForm):

    class Meta:
        model = JmboLink
        fields = [
            "title", "slug", "view_name", "view_params",
            "target_content_type", "target_object_id", "url"
        ]


