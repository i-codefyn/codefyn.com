from django.contrib import admin
from .models import OnlineRequest, ContactUs, FeedBack


class OnlineRequestAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "message",
    ]


admin.site.register(OnlineRequest, OnlineRequestAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "message",
    ]


admin.site.register(ContactUs, ContactUsAdmin)


class FeedBackAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "rating",
    ]


admin.site.register(FeedBack, FeedBackAdmin)
