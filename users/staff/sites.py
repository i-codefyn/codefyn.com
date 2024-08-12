from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# redirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

# generic import
from django.views.generic import (
    CreateView,
    DeleteView,
    View,
    TemplateView,
    ListView,
    DetailView,
    UpdateView,
)
from users.mixins import (
    TestMixinUserEmail,
    TestMixinUserName,
    StaffRequiredMixin,
    email_check,
)
from django.contrib.auth.decorators import user_passes_test

# alert Msg
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# date time
import datetime

# template loader
from django.template import loader

# 3RD Party
import csv

from sitesetting.models import Sites
from sitesetting.form import DateForm, StaffSitesForm
from users.staff.utils import render_to_pdf
from users.staff import app_settings


class SitesDelete(StaffRequiredMixin, TestMixinUserEmail, DeleteView):
    """site"""

    model = Sites
    template_name = "staff/dashboard/sites/list." + app_settings.TEMPLATE_EXTENSION
    success_url = reverse_lazy("site_list")
    success_message = "Site data Deleted !"
    context_object_name = "delete"
    login_url = reverse_lazy("login")


class SitesUpdate(StaffRequiredMixin, TestMixinUserEmail, UpdateView):
    """site update"""

    model = Sites
    success_message = " Setting successfully updated!"
    context_object_name = "sites"
    template_name = "staff/dashboard/sites/update." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("login")
    form_class = StaffSitesForm
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Site Settings",
        "page_title": app_settings.PAGE_TITLE,
    }


class SitesCreate(StaffRequiredMixin, TestMixinUserEmail, CreateView):
    """Sites Craete"""

    form_class = StaffSitesForm
    initial = {"key": "value"}
    template_name = "staff/dashboard/sites/create." + app_settings.TEMPLATE_EXTENSION
    login_url = "account_login"
    page_name = "Site Create"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            "form_sites": form,
            "app_data": Sites.objects.all(),
            "pagename": self.page_name,
            "page_title": app_settings.PAGE_TITLE,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, f"{self.page_name} - Successfully !")
        return reverse("site_list")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        context = {
            "form_sites": form,
            "app_data": Sites.objects.all(),
            "pagename": self.page_name,
            "page_title": app_settings.PAGE_TITLE,
        }
        return render(request, self.template_name, context)


class SitesDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """Slider Detail View"""

    model = Sites
    context_object_name = "sites"
    template_name = "staff/dashboard/sites/detail." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("login")
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "sites Details",
        "page_title": app_settings.PAGE_TITLE,
    }


class SitesList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """Slider List"""

    model = Sites
    template_name = "staff/dashboard/sites/list.html"
    login_url = "account_login"  # new
    form_class = DateForm
    context_object_name = "sites"
    extra_context = {
        "form_sites": form_class,
        "pagename": "Sites List",
        "app_data": Sites.objects.all(),
        "page_title": app_settings.PAGE_TITLE,
    }
