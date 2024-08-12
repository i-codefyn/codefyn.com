from django.forms import ModelForm
from django import forms
from .models import (
    Sites,
    Faq,
)
from django.forms import TextInput, FileInput, EmailInput


class FaqForm(ModelForm):
    """faq form"""

    class Meta:
        model = Faq
        fields = "__all__"


class StaffSitesForm(ModelForm):

    """sites setting form"""

    class Meta:
        model = Sites

        fields = [
            "display_name",
            "domain_name",
            "app_email",
            "app_mobile",
            "app_address",
            "app_version",
            "app_logo",
            "app_fevicon",
            "app_stamp",
        ]

        widgets = {
            "display_name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "display_name",
                }
            ),
            "domain_name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "domain name",
                }
            ),
            "app_email": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "app email",
                    "type": "email",
                }
            ),
            "app_mobile": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "app mobile",
                }
            ),
            "app_address": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "app address",
                }
            ),
            "app_version": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "app version",
                }
            ),
            "app_logo": FileInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "type": "file",
                }
            ),
        }


class DateForm(forms.Form):
    """date filter"""

    startdate = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "label": "From",
                "class": "form-control",
                "type": "date",
                "style": "width: 200px;",
            }
        )
    )
    enddate = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "label": "From",
                "class": "form-control",
                "type": "date",
                "style": "width: 200px;",
            }
        )
    )
