import time
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# redirects Imports
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# msg mixin import
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# template loader
from django.template import loader

# date  import
import datetime

# Generic Views Imports
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
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
from pages.models import OnlineRequest
from pages.form import OnlineRequestForm
from users.staff import app_settings
from datetime import date

# 3RD Party
# for pdf export
from users.staff.utils import render_to_pdf

# for csv export
import csv

# QR CODE
import io
import qrcode


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def OnlineRequestsExportCsv(request):
    """Online Requests Export CSV"""
    login_url = reverse_lazy("account_login")
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="onlinerequests.csv"'
    onlinerequests = OnlineRequest.objects.all()
    writer = csv.writer(response)
    for r in onlinerequests:
        writer.writerow(
            [
                "Name",
                "Mobile",
                "Email",
                "Device Name",
                "Device Problem",
                "Created Date",
            ]
        )
        writer.writerow(
            [
                r.name,
                r.mobile,
                r.email,
                r.device_name,
                r.device_problem,
                r.created_at,
            ]
        )
    return response


def qr_generate(data, size, version, border):
    qr = qrcode.QRCode(
        version=version,  # QR code version a.k.a size, None == automatic
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # lots of error correction
        box_size=size,  # size of each 'pixel' of the QR code
        border=border,  # minimum size according to spec
    )
    qr.add_data(data)
    img = qr.make_image()
    img_name = "qr" + str(time.time()) + ".png"
    img.save(settings.MEDIA_ROOT + "/" + img_name)

    return img_name


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def OnlineRequetsExportPdfbyId(request, pk):
    """Staff Online Request Export Pdf by id"""
    login_url = reverse_lazy("account_login")
    template_name = (
        "staff/dashboard/online_requests/reports/export_pdfbyid."
        + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = f'"{pk}"_online_requests.pdf'
    online_requests = OnlineRequest.objects.filter(id__gte=pk)
    # for QR COde
    size = 2
    version = 2
    border = 0
    for data in online_requests:
        name = data.name
        email = data.email
        mobile = data.mobile
        device = data.device_name
        problem = data.device_problem
        created = data.created_at
        # QR CODE GEN
        qr_data = {
            "Customer Name": data.name,
            "Email": data.email,
            "Mobile": data.mobile,
            "Device": data.device_name,
            "Problem": data.device_problem,
        }
        img_name = qr_generate(qr_data, size, version, border)
        pdf_name = f'"{data.name}"_online_requests.pdf'
        context = {
            "app_data": Sites.objects.all(),
            "name": name,
            "email": email,
            "mobile": mobile,
            "device": device,
            "problem": problem,
            "created": created,
            "time": datetime.date.today(),
            "doc_name": "Online Requests Detail",
            "img_name": img_name,
        }
        return render_to_pdf(template_name, context, pdf_name)


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def OnlineRequetsExportPdfbyDate(request):
    """Staff OnlineRequests Export Pdf by DATE"""
    login_url = reverse_lazy("account_login")
    template_name = (
        "staff/dashboard/online_requests/reports/export_pdf_bydate."
        + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = "online_request_filtered_list.pdf"

    if request.method == "POST":
        fromdate = request.POST.get("startdate")
        enddate = request.POST.get("enddate")
        data = OnlineRequest.objects.all().filter(
            created_at__gte=fromdate, created_at__lte=enddate
        )
        context = {
            "app_data": Sites.objects.all(),
            "OnlineRequests": data,
            "time": datetime.date.today(),
            "doc_name": "Online Requests",
        }
        return render_to_pdf(template_name, context, pdf_name)

    else:
        context = {
            "app_data": Sites.objects.all(),
            "OnlineRequests": OnlineRequest.objects.all(),
            "time": datetime.date.today(),
            "doc_name": "Online Requests",
        }
        return render_to_pdf(template_name, context, pdf_name)


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(email_check)
def OnlineRequestsExportPdfAll(request):
    """Online Request Export Pdf ALL"""
    login_url = reverse_lazy("account_login")
    template_name = (
        "staff/dashboard/online_requests/reports/export_pdfall."
        + app_settings.TEMPLATE_EXTENSION
    )
    pdf_name = "online_requests_list.pdf"
    context = {
        "app_data": Sites.objects.all(),
        "OnlineRequests": OnlineRequest.objects.all(),
        "time": datetime.date.today(),
        "doc_name": "Online Requests List",
    }
    return render_to_pdf(template_name, context, pdf_name)


class ViewOnlineRequestsByDate(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """Views Online Request By date"""

    form_class = DateForm
    model = OnlineRequest
    template_name = (
        "staff/dashboard/online_requests/list." + app_settings.TEMPLATE_EXTENSION
    )
    page_name = "Online Request"
    login_url = reverse_lazy("account_login")

    def post(self, request, *args, **kwargs):
        form = self.form_class
        if request.method == "POST":
            fromdate = request.POST.get("startdate")
            enddate = request.POST.get("enddate")
            online_requests = self.model.objects.all()

            if fromdate:
                data1 = online_requests.filter(created_at__gte=fromdate)
                context = {
                    "OnlineRequests": data1,
                    "form": form,
                    "app_data": Sites.objects.all(),
                    "pagename": self.page_name,
                    "page_title": app_settings.PAGE_TITLE,
                }
                return render(request, self.template_name, context)
            if enddate:
                data2 = online_requests.filter(created_at__lte=enddate)
                context = {
                    "OnlineRequests": data2,
                    "form": form,
                    "app_data": Sites.objects.all(),
                    "pagename": self.page_name,
                    "page_title": app_settings.PAGE_TITLE,
                }
                return render(request, self.template_name, context)
        else:
            form = self.form_class
            context = {
                "online_requests": self.model.objects.all(),
                "form": form,
            }
            return render(request, self.template_name, context)


class OnlineRequestDetails(StaffRequiredMixin, TestMixinUserEmail, DetailView):
    """DetailView"""

    model = OnlineRequest
    login_url = reverse_lazy("account_login")
    context_object_name = "online_requests"
    template_name = (
        "staff/dashboard/online_requests/detail." + app_settings.TEMPLATE_EXTENSION
    )
    data = "www.fixenix.com"
    # img = qrcode.make(data, box_size=2)
    # img_name = "qr" + str(time.time()) + ".png"
    # img.save(settings.MEDIA_ROOT + "/" + img_name)

    extra_context = {
        "app_data": Sites.objects.all(),
        "pagename": "Online Request Detail",
        "doc_name": "Online Request Detail",
        "date": datetime.date.today(),
        # "img_name": img_name,
    }


class OnlineRequestsList(StaffRequiredMixin, TestMixinUserEmail, ListView):
    """LIST VIEWS"""

    template_name = (
        "staff/dashboard/online_requests/list." + app_settings.TEMPLATE_EXTENSION
    )
    login_url = reverse_lazy("account_login")
    model = OnlineRequest
    form_class = DateForm
    context_object_name = "OnlineRequests"
    extra_context = {
        "form": form_class,
        "app_data": Sites.objects.all(),
        "pagename": "Online Requests",
        "page_title": app_settings.PAGE_TITLE,
    }
