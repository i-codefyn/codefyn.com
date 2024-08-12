from django.contrib import admin

from .models import Services,Reviews


class ReviewInline(admin.TabularInline):
    model = Reviews


class ServicesAdmin(admin.ModelAdmin):

    inlines = [
        ReviewInline,
    ]
    list_display = ('service_name','service_for','service_price',)



admin.site.register(Services,ServicesAdmin)
