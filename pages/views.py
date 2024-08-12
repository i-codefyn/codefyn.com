# time
from django.utils import timezone
import datetime

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
import re

# settingd imports
from django.conf import settings
from . import app_setting

# mail
from django.core.mail import EmailMultiAlternatives  # form html send
from django.core.mail import send_mail

# template rendering
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
# jason response
from django.http import JsonResponse

# appp imports views
from django.views.generic import TemplateView, CreateView, View, FormView, ListView
from django.views.generic.detail import SingleObjectMixin
from sitesetting.models import (
    Faq,
)

# app import models
from .models import OnlineRequest, ContactUs, FeedBack

# app imoprt forms
from .form import OnlineRequestForm, ContactForm, FeedBackForm, OtpVerifyForm



class LatestDesignsView(TemplateView):
    template_name = "home/latest-designs." + app_setting.TEMPLATE_EXTENSION
    PAGE_TITLE = "Latest Degins"
    extra_context = {
        "page_title": PAGE_TITLE,
    }




class ProjectDiscussFormView(SuccessMessageMixin, View):
    """HomePage View"""

    template_name = "home/quote_form." + app_setting.TEMPLATE_EXTENSION
    model = OnlineRequest
    form_class = OnlineRequestForm


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                "form": form,
                "page_title": "Enquiry Form",
            },
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self, to_mail):
        messages.success(self.request, f"OTP is Sent to {to_mail}")
        return reverse("Home:otp_verify")

    def form_valid(self, form):
        """if from data is valid"""

        if self.request.method == "POST":
            if form.is_valid():
                n = form.cleaned_data["name"]
                e = form.cleaned_data["email"]
                mo = form.cleaned_data["mobile"]
                # c = form.cleaned_data["company_name"]
                # w = form.cleaned_data["webtype"]
                p = form.cleaned_data["services"]
                m = form.cleaned_data["message"]
                self.request.session["name"] = n
                self.request.session["email"] = e
                self.request.session["mobile"] = mo
                # self.request.session["company_name"] = c
                # self.request.session["webtype"] = w
                self.request.session["services"] = p
                self.request.session["message"] = m
                from_mail = settings.EMAIL_HOST_USER
                to_mail = e
                otp = randomDigits(4)
                expiry = get_expiry()
                self.request.session["otp"] = otp
                self.request.session["time"] = str(expiry)
                template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
                subject = "Email Verifiaction Code"
                context = {
                    "title": "Email Verification Code",
                    "content": f"your OTP is {otp} .Dont share with anyone",
                }

                SendHTMLMail(subject, context, template_name, to_mail, from_mail)
                # self.request.session.set_expiry(100)
                return HttpResponseRedirect(self.get_success_url(to_mail))

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        context = {
            "form": form,
            "page_title": "Home Page",
        }
        for error in errors:
            messages.error(self.request, f"Please Check {error}-& Try Again")
            return render(self.request, self.template_name, context)


def OtpReset(request):
    otp = randomDigits(4)
    expiry = get_expiry()
    request.session["otp"] = otp
    request.session["time"] = str(expiry)
    from_mail = settings.EMAIL_HOST_USER
    to_mail = request.session["email"]
    template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
    subject = "OTP for Final Submit"
    context = {
        "title": "OTP For Email Varifiaction",
        "content": f"your OTP is {otp} .Dont share with anyone",
    }
    SendHTMLMail(subject, context, template_name, to_mail, from_mail)
    message = f"OTP  is Sent to Your {to_mail}"
    messages.success(request, message)
    return HttpResponseRedirect(reverse_lazy("Home:otp_verify"))


class OtpVerify(View):
    form_class = OtpVerifyForm
    initial = {"key": "value"}
    template_name = "home/otpverify." + app_setting.TEMPLATE_EXTENSION
    model = OnlineRequest

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
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
        name = self.request.session["name"]
        message = self.request.session.get("message")
        mobile = self.request.session.get("mobile")
        # company_name = self.request.session.get("company_name")
        # webtype = self.request.session.get("webtype")
        services = self.request.session.get("services")
        email_address = self.request.session.get("email")
        expriry = self.request.session.get("time")
        _now = str(timezone.now())
        if int(otp) == int(u_otp) and (_now < expriry):
            OnlineRequest.objects.create(
                name=name,
                mobile=mobile,
                # company_name=company_name,
                email=email_address,
                # webtype=webtype,
                services=services,
                message=message,
            )
            from_mail = settings.EMAIL_HOST_USER
            to_mail = app_setting.EMAIL_CC
            template_name = "email/online_request." + app_setting.TEMPLATE_EXTENSION
            subject = "New Online Requests"
            context = {
                "title": "Online Requests",
                "name": name,
                "mobile": mobile,
                # "company_name": company_name,
                "email": email_address,
                # "webtype": webtype,
                "services": services,
                "messages": messages,
                "date": datetime.datetime.now(),
            }
            SendHTMLMail(subject, context, template_name, to_mail, from_mail)
            self.request.session.delete("otp")
            self.request.session.delete("name")
            self.request.session.delete("mobile")
            # self.request.session.delete("company_name")
            # self.request.session.delete("webtype")
            self.request.session.delete("services")
            self.request.session.delete("email")
            self.request.session.delete("message")
            messages.success(self.request, "Request Successfully Submited ! Thank You")
            return JsonResponse({"messages": "success"}, status=200)
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


class HomePageView(TemplateView):
    template_name = "home/index." + app_setting.TEMPLATE_EXTENSION
    PAGE_TITLE = "Home Page"
    extra_context = {
        "page_title": PAGE_TITLE,
    }



class RefundPolicyView(TemplateView):
    template_name = "home/refund_policy." + app_setting.TEMPLATE_EXTENSION
    PAGE_TITLE = "Refund Policy"
    extra_context = {
        "page_title": PAGE_TITLE,
    }


class PrivacyPolicyView(TemplateView):
    template_name = "home/privacy_policy." + app_setting.TEMPLATE_EXTENSION
    PAGE_TITLE = "Privacy Policy"
    extra_context = {
        "page_title": PAGE_TITLE,
    }


class ContactFormView(View):
    template_name = "home/contact_us." + app_setting.TEMPLATE_EXTENSION
    form_class = ContactForm
    PAGE_TITLE = "Contact Page"
    extra_context = {
        "page_title": PAGE_TITLE,
    }

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        contex = {
            "form_contact": form,
            "page_title": "Contact_Us",
        }

        return render(request, self.template_name, contex)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Thank You For Writting Us !")
        return reverse("Home:contactus")

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        form.save(commit=False)
        from_mail = settings.EMAIL_HOST_USER
        to_mail = app_setting.EMAIL_CC
        template_name = "email/enquiry." + app_setting.TEMPLATE_EXTENSION
        subject = "Enquiry"
        context = {
            "title": "Online Enquiry",
            "name": name,
            "email": email,
            "msg": message,
            "date": datetime.datetime.now(),
        }
        SendHTMLMail(subject, context, template_name, to_mail, from_mail)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        context = {
            "form_contact": form,
            "page_title": "Contact_Us",
            "errors": errors,
        }
        for error in errors:
            messages.error(self.request, f"Please Check - {error} & Try Again ")
            return render(self.request, self.template_name, context)


class FeedBackFormView(FormView):
    template_name = "home/feedback." + app_setting.TEMPLATE_EXTENSION
    form_class = FeedBackForm
    PAGE_TITLE = "Feedback"
    extra_context = {
        "page_title": PAGE_TITLE,
    }

    def get_success_url(self):
        messages.success(self.request, "Thank You For Feedback !")
        return reverse("Home:feedback")

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        email = form.cleaned_data["email"]
        form.save(commit=False)
        from_mail = settings.EMAIL_HOST_USER
        to_mail = app_setting.EMAIL_CC
        template_name = "email/feedback." + app_setting.TEMPLATE_EXTENSION
        subject = "Feedback"
        context = {
            "title": "Feedback",
            "email": email,
            "date": datetime.datetime.now(),
        }
        SendHTMLMail(subject, context, template_name, to_mail, from_mail)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        context = {
            "form": form,
            "page_title": "Feedback",
            "errors": errors,
        }
        for error in errors:
            messages.error(self.request, f"Please Check - {error} & Try Again ")
            return render(self.request, self.template_name, context)


class OurWorks(TemplateView):
    PAGE_TITLE = "Our Works"
    template_name = "home/works." + app_setting.TEMPLATE_EXTENSION
    extra_context = {
        "page_tite": PAGE_TITLE,
    }


class AboutUs(TemplateView):
    PAGE_TITLE = "Home Page"
    template_name = "home/about_us." + app_setting.TEMPLATE_EXTENSION
    extra_context = {
        "page_tite": PAGE_TITLE,
    }


def SendMail(SenderMail, message, RecieverEmail):
    subject = (f"Thank You For Writting Us!",)
    message = message
    from_email = SenderMail
    recipient_list = [RecieverEmail]
    return send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )


def SendOtp(email, message, e):
    subject = ("Otp",)
    message = message
    from_email = email
    recipient_list = [e]
    return send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )


class DisclamerView(TemplateView):
    template_name = "home/Disclamer." + app_setting.TEMPLATE_EXTENSION
    extra_context = {"page_title": "disclamer"}


class TermsAndConditionsView(TemplateView):
    """
    Terms And Conditions
    """

    template_name = "home/terms_conditions." + app_setting.TEMPLATE_EXTENSION
    extra_context = {"page_title": "Terms & Conditions"}


class FaqsView(TemplateView):
    """FAQs Views"""
    template_name = "home/faqs." + app_setting.TEMPLATE_EXTENSION
    extra_context = {"page_title": "FAQ's"}
# class FaqsView(ListView):
#     """FAQs Views"""

#     PAGE_TITLE = "FAQs"
#     template_name = "home/faqs." + app_setting.TEMPLATE_EXTENSION
#     # paginate_by = 100  # if pagination is desired
#     model = Faq
#     context_object_name = "faq"
#     extra_context = {
#         "page_tite": PAGE_TITLE,
#     }


def SendHTMLMail(subject, context, template_name, to_mail, from_mail):
    """Html Send Through Email"""
    context = context
    subject = subject
    html_content = render_to_string(template_name, context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_mail, [to_mail])
    email.attach_alternative(html_content, "text/html")
    return email.send()


def randomDigits(digits):
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
