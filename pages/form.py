from django.forms import ModelForm
from django import forms
from django.forms import TextInput, FileInput, EmailInput, Textarea, NumberInput
from .models import OnlineRequest, ContactUs, FeedBack

from captcha.fields import CaptchaField, CaptchaTextInput

import re

REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


class FeedBackForm(ModelForm):
    """Feedback form"""

    captcha = CaptchaField(
        widget=CaptchaTextInput(
            attrs={
                "placeholder": "Type Captcha",
            }
        )
    )

    class Meta:
        model = FeedBack
        fields = ["email", "rating"]
        widgets = {
            "email": TextInput(
                attrs={
                    "class": "form-control ",
                    "style": "",
                    "placeholder": "Email",
                    "id": "floatingInput",
                }
            ),
            "rating": TextInput(
                attrs={
                    "class": "rate",
                    "style": "",
                    "placeholder": "rating",
                    "id": "floatingInput",
                    "type": "radio",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and not re.match(REGEX, email):
            raise forms.ValidationError("Invalid email format")
        return email


class ContactForm(ModelForm):
    """contact form"""

    captcha = CaptchaField(
        widget=CaptchaTextInput(
            attrs={
                "placeholder": "Type Captcha",
            }
        )
    )

    class Meta:
        model = ContactUs
        fields = ["name", "email", "message"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:50px; color:blue; font-weight:500; ",
                    "placeholder": "Name",
                    "id": "floatingInput",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:50px; color:blue; font-weight:500; ",
                    "placeholder": "Email",
                    "id": "floatingInput",
                    "type": "email",
                }
            ),
            "message": Textarea(
                attrs={
                    "class": "form-control ",
                    "style": "padding-left:50px; color:blue; font-weight:500; height:120px;",
                    "placeholder": "message",
                    "id": "floatingInput",
                }
            ),
        }
        # this function will be used for the validation

    def clean(self):
        # data from the form is fetched using super function
        super(ContactForm, self).clean()
        # extract the username and text field from the data
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        message = self.cleaned_data.get("message")

        # conditions to be met for the name length
        if len(name) < 5:
            self._errors["name"] = self.error_class(["Minimum 5 characters required"])
        if len(message) < 10:
            self._errors["message"] = self.error_class(
                ["Message Should Contain a minimum of 10 characters"]
            )
            # return any errors if found
        return self.cleaned_data


class OtpVerifyForm(forms.Form):
    """otp submit form"""

    captcha = CaptchaField(
        widget=CaptchaTextInput(
            attrs={
                "placeholder": "Type Captcha",
            }
        )
    )
    otp1 = forms.CharField(
        max_length=1,
        required=True,
        widget=NumberInput(
            attrs={
                "type": "",
                "class": "form-control",
                "placeholder": "*",
                "style": "padding-left:20px;",
            }
        ),
    )
    otp2 = forms.CharField(
        max_length=1,
        required=True,
        widget=NumberInput(
            attrs={
                "type": "",
                "class": "form-control",
                "placeholder": "*",
                "style": "padding-left:20px;",
            }
        ),
    )
    otp3 = forms.CharField(
        max_length=1,
        required=True,
        widget=NumberInput(
            attrs={
                "type": "",
                "class": "form-control",
                "placeholder": "*",
                "style": "padding-left:20px;",
            }
        ),
    )
    otp4 = forms.CharField(
        max_length=1,
        required=True,
        widget=NumberInput(
            attrs={
                "type": "",
                "class": "form-control",
                "placeholder": "*",
                "style": "padding-left:20px;",
            }
        ),
    )

    def clean(self):
        # data from the form is fetched using super function
        super(OtpVerifyForm, self).clean()
        otp1 = self.cleaned_data.get("otp1")
        otp2 = self.cleaned_data.get("otp2")
        otp3 = self.cleaned_data.get("otp3")
        otp4 = self.cleaned_data.get("otp4")

        # conditions to be met for the length
        if len(otp1) > 1:
            self._errors["otp1"] = self.error_class(["Only Single Digit"])
        if len(otp2) > 1:
            self._errors["otp2"] = self.error_class(["Only Single Digit"])
        if len(otp3) > 1:
            self._errors["otp3"] = self.error_class(["Only Single Digit"])
        if len(otp4) > 1:
            self._errors["otp4"] = self.error_class(["Only Single Digit"])


WEB_CHOICES = (
    ("Static", "Static Websites"),
    ("Dynamic", "Dynamic Website"),
    ("E-Commerce", "E-Commerce"),
    ("Corporate", "Corporate Website"),
)
PACK_CHOICES = (
    ("Stater", "Stater Pack"),
    ("Extended", "Extended Pack"),
    ("Pros", "Pros Pack"),
)
SERVICES_CHOICES = (
    ("Website Development", "Website development"),
    ("E-commerce", "E-commerce"),
    ("Software Development", "Software development"),
    ("Logo Design", "Logo Design"),
    ("Graphics Design", "Graphics Design"),
    ("Domain Registrty", "Domain Registrty"),
    ("Digital Marketing", "Digital Marketing"),
    ("SEO", "SEO"),
)


class OnlineRequestForm(ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    # webtype = forms.CharField(
    #     widget=forms.Select(
    #         choices=WEB_CHOICES,
    #         attrs={
    #             "class": "form-control form-select",
    #             "style": " font-weight:500; ",
    #             "id": "floatingInput",
    #         },
    #     )
    # )
    # packages = forms.CharField(
    #     widget=forms.Select(
    #         choices=PACK_CHOICES,
    #         attrs={
    #             "class": "form-control form-select",
    #             "style": " font-weight:500; ",
    #             "id": "floatingInput",
    #         },
    #     )
    # )
    captcha = CaptchaField(
        widget=CaptchaTextInput(
            attrs={
                "placeholder": "Type Captcha",
            }
        )
    )
    services = forms.CharField(
        widget=forms.Select(
            choices=SERVICES_CHOICES,
            attrs={
                "class": "form-control form-select",
                "style": " font-weight:500; ",
                "id": "floatingInput",
            },
        )
    )

    class Meta:
        model = OnlineRequest
        fields = [
            "name",
            "email",
            "mobile",
            "services",
            "message",
        ]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; color:blue; font-weight:500; ",
                    "placeholder": "Name",
                    "id": "floatingInput",
                }
            ),
            "mobile": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; color:blue; font-weight:500; ",
                    "placeholder": "Name",
                    "id": "floatingInput",
                }
            ),
            "company_name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; color:blue; font-weight:500; ",
                    "placeholder": "Name",
                    "id": "floatingInput",
                }
            ),
            "email": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; color:blue; font-weight:500; ",
                    "placeholder": "Email",
                    "id": "floatingInput",
                }
            ),
            "message": Textarea(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:40px; color:blue; font-weight:500; ",
                    "placeholder": "Project Idea ..!",
                    "id": "floatingInput",
                }
            ),
        }

    def clean(self):
        # data from the form is fetched using super function
        super(OnlineRequestForm, self).clean()
        # extract the username and text field from the data
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        message = self.cleaned_data.get("message")

        # conditions to be met for the name length
        if len(name) < 5:
            self._errors["name"] = self.error_class(["Minimum 5 characters required"])

        if len(message) < 10:
            self._errors["message"] = self.error_class(
                ["Message Should Contain a minimum of 10 characters"]
            )
            # return any errors if found
        return self.cleaned_data
