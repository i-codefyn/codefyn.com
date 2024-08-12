from django.conf import settings
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

# LOCAL
from users.staff.utils import render_to_pdf
from users.staff import app_settings
from sitesetting.form import DateForm
from sitesetting.models import Sites
from users.models import CustomUser

import csv


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def UsersExportPdfbyDate(request):
    """Staff User Export Pdf by DATE"""
    template_name = (
        "staff/dashboard/users/reports/export_pdfall." + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = "users_list.pdf"
    time = datetime.date.today()
    if request.method == "POST":
        fromdate = request.POST.get("startdate")
        enddate = request.POST.get("enddate")
        data = CustomUser.objects.all().filter(
            date_joined__gte=fromdate, date_joined__lte=enddate
        )
        return render_to_pdf(
            template_name,
            {
                "app_data": Sites.objects.all(),
                "data": data,
                "time": time,
                "doc_name": "users List",
            },
            pdf_name,
        )
    else:
        datas = CustomUser.objects.all()
        return render_to_pdf(
            template_name,
            {
                "app_data": Sites.objects.all(),
                "data": datas,
                "time": time,
                "doc_name": "users List",
            },
            pdf_name,
        )


class UsersList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """Staff Users Views By date"""

    template_name = "staff/dashboard/users/list." + app_settings.TEMPLATE_EXTENSION
    form_class = DateForm
    model = CustomUser
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        contex = {
            "form": form,
            "users": self.model.objects.all(),
            "pagename": "Users List",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
            "user_count": self.model.count(),
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
        users = self.model.objects.all()
        context = {
            "users": users.filter(created_at__gte=fromdate),
            "form": form,
            "app_data": Sites.objects.all(),
            "pagename": "Users List",
            "app_data": Sites.objects.all(),
            "page_title": app_settings.PAGE_TITLE,
        }
        if fromdate:
            return render(self.request, self.template_name, context)
        if enddate:
            context = {
                "users": users.filter(created_at__lte=enddate),
                "form": form,
                "pagename": "Users List",
                "app_data": Sites.objects.all(),
                "page_title": app_settings.PAGE_TITLE,
            }
            return render(request, self.template_name, context)

    def form_invalid(self, form):
        form = DateForm
        data = self.model.objects.all()
        return render(
            request,
            self.template_name,
            {
                "users": data,
                "form": form,
            },
        )


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def UsersExportCsv(request):
    """Users Export CSV"""
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="users.csv"'
    users = CustomUser.objects.all()
    writer = csv.writer(response)
    for u in users:
        writer.writerow(
            [
                "Username",
                "Email",
            ]
        )
        writer.writerow(
            [
                u.username,
                u.email,
            ]
        )
    return response


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def UsersExportPdfbyId(request, pk):
    """Users Export Pdf by id"""
    template_name = (
        "staff/dashboard/users/reports/export_pdfbyid."
        + app_settings.TEMPLATE_EXTENSION
    )
    users = CustomUser.objects.filter(id__gte=pk)
    pdf_name = f'"{pk}"user.pdf'
    time = datetime.date.today()
    return render_to_pdf(
        template_name,
        {
            "app_data": Sites.objects.all(),
            "users": users,
            "time": time,
            "doc_name": "User List",
        },
        pdf_name,
    )


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def UsersExportPdfAll(request):
    """Users Export Pdf all"""
    template_name = (
        "staff/dashboard/users/reports/export_pdfall." + app_settings.TEMPLATE_EXTENSION
    )
    data = CustomUser.objects.all()
    pdf_name = "users_list.pdf"
    time = datetime.date.today()
    return render_to_pdf(
        template_name,
        {
            "app_data": Sites.objects.all(),
            "data": data,
            "time": time,
            "doc_name": "Users List",
        },
        pdf_name,
    )


class UsersDetail(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """Users Detail view"""

    model = CustomUser
    context_object_name = "users"
    template_name = "staff/dashboard/users/detail." + app_settings.TEMPLATE_EXTENSION
    login_url = "account_login"
    extra_context = {
        "page_title": app_settings.PAGE_TITLE,
        "pagename": "Users Details",
        "app_data": Sites.objects.all(),
    }
