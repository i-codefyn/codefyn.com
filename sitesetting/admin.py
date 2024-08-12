from django.contrib import admin
from .models import (
    Sites,
    Faq,
)


class SitesAdmin(admin.ModelAdmin):
    list_display = (
        "domain_name",
        "display_name",
        "app_version",
        "app_logo",
        "app_fevicon",
        "app_email",
        "app_mobile",
        "app_address",
        "app_version",
        "app_stamp",
    )


admin.site.register(Sites, SitesAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ("que", "ans")


admin.site.register(Faq, FaqAdmin)
