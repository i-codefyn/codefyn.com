# Login mixin imports


from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin

# redirects Imports
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# msg mixin import

# Generic Views Imports
from django.views.generic import ListView, DetailView

from users.mixins import (
    TestMixinUserEmail,
    TestMixinUserName,
    StaffRequiredMixin,
    email_check,
)
from django.contrib.auth.decorators import user_passes_test

# local Imports
from sitesetting.models import Sites
from sitesetting.form import DateForm
from pages.models import FeedBack, ContactUs

from users.staff import app_settings


class MessageDetails(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """DetailView"""

    model = FeedBack
    login_url = reverse_lazy("login")
    context_object_name = "Feedback  Detail"
    template_name = "staff/dashboard/messages/detail." + app_settings.TEMPLATE_EXTENSION

    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Feedback detail",
    }


class MessageList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """Views By date"""

    form_class = DateForm
    model = ContactUs
    template_name = "staff/dashboard/messages/list." + app_settings.TEMPLATE_EXTENSION
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        contex = {
            "form": form,
            "msg": self.model.objects.all(),
            "pagename": "Message List",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
        }

        return render(request, self.template_name, contex)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if request.method == "POST":
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        fromdate = self.request.POST.get("startdate")
        enddate = self.request.POST.get("enddate")
        context = {
            "msg": self.model.objects.all().filter(created_at__gte=fromdate),
            "form": form,
            "app_data": Sites.objects.all(),
            "pagename": "Message list",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
        }
        if fromdate:
            return render(self.request, self.template_name, context)
        if enddate:
            context = {
                "msg": self.model.objects.all().filter(created_at__lte=enddate),
                "form": form,
                "pagename": "Message List",
                "app_data": Sites.objects.all(),
                "page_title": app_settings.PAGE_TITLE,
            }
            return render(request, self.template_name, context)

    def form_invalid(self, form):
        return render(
            request,
            self.template_name,
            {
                "msg": self.model.objects.all(),
                "form": form,
            },
        )
