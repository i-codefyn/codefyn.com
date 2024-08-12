from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# alert msg
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# generic import
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView,
)
from users.mixins import (
    TestMixinUserEmail,
    TestMixinUserName,
    StaffRequiredMixin,
    email_check,
)
from django.contrib.auth.decorators import user_passes_test

# local  import
from users.staff import app_settings
from sitesetting.models import Sites, Faq
from sitesetting.form import FaqForm


class FaqDelete(StaffRequiredMixin, TestMixinUserEmail, DeleteView):
    """DeleteView"""

    template_name = "staff/dashboard/faq/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = Faq
    context_object_name = "delete"
    success_url = reverse_lazy("faq_list")
    success_message = "Item Deleted Successfully !"


class FaqUpdate(StaffRequiredMixin, TestMixinUserEmail, UpdateView):
    """UpadteView"""

    template_name = "staff/dashboard/faq/update." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = Faq
    success_url = reverse_lazy("faq_list")
    success_message = "Data Updated Successfully !"
    form_class = FaqForm
    context_object_name = "faq"
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "FAQs",
        "page_title": app_settings.PAGE_TITLE,
    }


class FaqDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """DetailView"""

    template_name = "staff/dashboard/faq/detail." + app_settings.TEMPLATE_EXTENSION
    model = Faq
    login_url = reverse_lazy("account_login")
    context_object_name = "faq"
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "FAQs",
        "page_title": app_settings.PAGE_TITLE,
    }


class FaqCreate(StaffRequiredMixin, TestMixinUserEmail, CreateView):
    """CreateView"""

    template_name = "staff/dashboard/faq/Create." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = Faq
    form_class = FaqForm
    initial = {"key": "value"}

    def get(self, request, *agrs, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(
            self.request,
            self.template_name,
            {
                "form": form,
                "app_data": Sites.objects.all(),
                "faq": Faq.objects.all(),
                "pagename": "Faq",
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        from django.contrib import messages

        messages.success(self.request, "Addedd Successfully !")
        return reverse("faq_list")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return render(
            self.request,
            self.template_name,
            {
                "form": form,
                "app_data": Sites.objects.all(),
                "pagename": "Faq",
            },
        )


class FaqList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """LIST VIEWS"""

    template_name = "staff/dashboard/faq/list." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    model = Faq
    context_object_name = "faq"
    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "FAQs",
        "page_title": app_settings.PAGE_TITLE,
    }
