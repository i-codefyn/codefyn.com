from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from allauth.account.forms import SignupForm, LoginForm
from django.forms import TextInput, FileInput, EmailInput, Textarea, NumberInput
from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class CustomLoginForm(LoginForm):
    captcha = CaptchaField(
        widget=CaptchaTextInput(
            attrs={
                "placeholder": "Type Captcha",
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"].widget.attrs["class"] = "form-control form-signup"
        self.fields["password"].widget.attrs["class"] = "form-control form-signup"
        self.fields["login"].label = ""
        self.fields["password"].label = ""
        self.fields["captcha"].label = ""

    def login(self, *args, **kwargs):
        return super(CustomLoginForm, self).login(*args, **kwargs)


class CustomSignupForm(SignupForm):
    captcha = CaptchaField(
        widget=CaptchaTextInput(
            attrs={
                "placeholder": "Type Captcha",
            }
        )
    )

    field_order = ["username", "email", "password1", "captcha"]

    # Override the init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["captcha"].label = ""
        self.fields["username"].widget = forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control form-signup",
                "type": "text",
            }
        )
        self.fields["email"].widget = forms.TextInput(
            attrs={
                "placeholder": "E-mail",
                "class": "form-control form-signup",
                "type": "email",
            }
        )
        self.fields["password1"].widget = forms.TextInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-signup",
                "type": "password",
            }
        )

    def custom_signup(self, request, user):
        user.save()


class UserVerifyForm(forms.Form):
    captcha = CaptchaField(
        widget=CaptchaTextInput(
            attrs={
                "placeholder": "Type Captcha",
            }
        )
    )


class CodeVerifyForm(forms.Form):
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
        super(CodeVerifyForm, self).clean()
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


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
