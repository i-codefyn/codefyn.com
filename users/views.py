from django.conf import settings
from pathlib import Path
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

# revers and redirect
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# validation
from django.core.exceptions import ValidationError

# random number
import random

# requests
import requests

# mail
from django.core.mail import EmailMultiAlternatives  # form html send


# template rendering
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# jason response
from django.http import JsonResponse
from django.views.generic import CreateView, TemplateView, ListView, FormView, View
from .models import CustomUser
from pages.models import OnlineRequest
from pages.models import FeedBack, ContactUs


from users import app_settings
from users.mixins import TestMixinUserEmail, TestMixinUserName, StaffRequiredMixin

import random

# All auth signup
from allauth.account.views import SignupView

from .forms import CustomUserCreationForm, UserVerifyForm, CodeVerifyForm
from django.db.models import Count


class StaffView(StaffRequiredMixin, TestMixinUserEmail, TemplateView):
    template_name = "staff/dashboard/dashboard." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    success_message = " Login Success !"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["user_count"] = CustomUser.objects.count()
        context["online_request_count"] = CustomUser.objects.count()
        context["feedback_count"] = FeedBack.objects.count()
        context["msg_count"] = ContactUs.objects.count()
        return context

    extra_context = {
        "site_name": app_settings.SITE_NAME,
        "page_title": app_settings.PAGE_TITLE,
    }


class UserAcountView(LoginRequiredMixin, TemplateView):
    template_name = "account/dashboard/user_account." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")


class UserCodeVerify(LoginRequiredMixin, FormView):
    form_class = CodeVerifyForm
    template_name = "account/verify/code_verify." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    extra_context = {"page_title": app_settings.PAGE_TITLE}

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        """otp submit"""
        a = form.cleaned_data["otp1"]
        b = form.cleaned_data["otp2"]
        c = form.cleaned_data["otp3"]
        d = form.cleaned_data["otp4"]
        list = [a, b, c, d]
        s = [str(i) for i in list]
        u_otp = int("".join(s))
        otp = self.request.session.get("otp")
        email_address = self.request.session.get("email")
        expriry = self.request.session.get("time")
        _now = str(timezone.now())
        if int(otp) == int(u_otp) and (_now < expriry):
            self.request.session.delete("email")
            messages.success(self.request, "Varification Success !")
            return HttpResponseRedirect(reverse_lazy("user_dashboard"))
        else:
            if _now > expriry:
                error = "Otp Expired ! Try Again"
                messages.error(self.request, error)
                return JsonResponse({"errors": error}, status=400)

            error = f"Please Put Valid OTP"
            messages.error(self.request, error)
            return JsonResponse({"errors": error}, status=400)

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        for error in errors:
            return JsonResponse({"errors": error}, status=400)


class UserVerify(LoginRequiredMixin, FormView):
    login_url = reverse_lazy("account_login")
    template_name = "email/emails." + app_settings.TEMPLATE_EXTENSION

    def get_success_url(self, to_mail):
        message = f"Otp Has Sent to Your Email {to_mail}"
        messages.success(self.request, message)
        return reverse("user_code_verify")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            from_mail = settings.EMAIL_HOST_USER
            to_mail = request.user.email
            otp = random_digits(4)
            expiry = get_expiry()
            self.request.session["otp"] = otp
            self.request.session["time"] = str(expiry)
            subject = "OTP for User Varification "
            context = {
                "title": "User Varification Verification Code",
                "content": f"your OTP is {otp} .Dont share with anyone",
            }
            try:
                SendHTMLMail(subject, context, self.template_name, to_mail, from_mail)
                return HttpResponseRedirect(self.get_success_url(to_mail))
            except:
                messages.error(self.request, "Code Not Sent")
                return HttpResponseRedirect(reverse_lazy("user_verify"))


class StaffVerify(StaffRequiredMixin, TestMixinUserEmail, FormView):
    login_url = reverse_lazy("account_login")

    def get_success_url(self, to_mail):
        messages.success(self.request, f"Otp Has Sent to Your Email {to_mail}")
        return reverse("staff_code_verify")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            from_mail = settings.EMAIL_HOST_USER
            to_mail = request.user.email
            otp = random_digits(4)
            expiry = get_expiry()
            self.request.session["otp"] = otp
            self.request.session["time"] = str(expiry)
            template_name = "email/emails." + app_settings.TEMPLATE_EXTENSION
            subject = "OTP for User Varification "
            context = {
                "title": "User Varification Verification Code",
                "content": f"your OTP is {otp} .Dont share with anyone",
            }
            try:
                SendHTMLMail(subject, context, template_name, to_mail, from_mail)
                return HttpResponseRedirect(self.get_success_url(to_mail))
            except:
                messages.error(self.request, "Code Not Sent")
                return HttpResponseRedirect(reverse_lazy("user_verify"))


class StaffCodeVerify(StaffRequiredMixin, TestMixinUserEmail, FormView):
    form_class = CodeVerifyForm
    template_name = "staff/verify/code_verify." + app_settings.TEMPLATE_EXTENSION
    login_url = reverse_lazy("account_login")
    extra_context = {"page_title": app_settings.PAGE_TITLE}

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        """otp submit"""
        a = form.cleaned_data["otp1"]
        b = form.cleaned_data["otp2"]
        c = form.cleaned_data["otp3"]
        d = form.cleaned_data["otp4"]
        list = [a, b, c, d]
        s = [str(i) for i in list]
        u_otp = int("".join(s))
        otp = self.request.session.get("otp")
        email_address = self.request.session.get("email")
        expriry = self.request.session.get("time")
        _now = str(timezone.now())
        if int(otp) == int(u_otp) and (_now < expriry):
            self.request.session.delete("email")
            messages.success(self.request, "Varification Success !")
            return HttpResponseRedirect(reverse_lazy("staff"))
        else:
            if _now > expriry:
                error = "Otp Expired ! Try Again"
                messages.error(self.request, error)
                return JsonResponse({"errors": error}, status=400)

            error = f"Please Put Valid OTP "
            messages.error(self.request, error)
            return JsonResponse({"errors": error}, status=400)

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        for error in errors:
            return JsonResponse({"errors": error}, status=400)


def SendHTMLMail(subject, context, template_name, to_mail, from_mail):
    """Html Send Through Email"""
    context = context
    subject = subject
    html_content = render_to_string(template_name, context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_mail, [to_mail])
    email.attach_alternative(html_content, "text/html")
    return email.send()


# class SignupPageView(SignupView):
#     template_name = "signu." + app_settings.TEMPLATE_EXTENSION


def random_digits(digits):
    lower = 10 ** (digits - 1)
    upper = 10**digits - 1
    at = random.randint(lower, upper)
    return at


def get_expiry():
    now = timezone.now()
    expiry_seconds = 120
    expiry_time = timezone.timedelta(seconds=expiry_seconds)
    expiry = now + expiry_time
    return expiry


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


# Create your views here.
