from django.conf import settings
from django.urls import reverse_lazy
from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        # write your logic here
        if self.request.user.is_superuser:
            path = "staff_verify"
            return reverse_lazy(path.format(username=request.user.username))
        # write your logic here
        if self.request.user.is_staff:
            path = "staff_verify"
            return reverse_lazy(path.format(username=request.user.username))

        if self.request.user:
            path = "user_verify"
            return reverse_lazy(path.format(username=request.user.username))

    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.

        Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse
        """
        return False
