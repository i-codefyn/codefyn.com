from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from users import app_settings


def email_check(user):
    return user.email.endswith(app_settings.USER_START_WITH)


class TestMixinUserEmail(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.email.endswith(app_settings.USER_START_WITH)


class TestMixinUserName(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.username.startswith(app_settings.USERNAME_START_WITH)


class StaffRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy("account_login")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(
                request,
                "You do not have the permission required to perform the "
                "requested operation.",
            )
            return redirect(settings.LOGIN_URL)
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class SuperUserRequiredMixin(LoginRequiredMixin):
    """
    View mixin which requires that the authenticated user is a super user
    (i.e. `is_superuser` is True).
    """

    login_url = reverse_lazy("account_login")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(
                request,
                "You do not have the permission required to perform the "
                "requested operation.",
            )
            return redirect(settings.LOGIN_URL)
        return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)
