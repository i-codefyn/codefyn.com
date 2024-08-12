from django.urls import path

from users.views import (
    SignupPageView,
    UserVerify,
    StaffVerify,
    UserCodeVerify,
    StaffCodeVerify,
    UserAcountView,
)


urlpatterns = [
    path("staff-verify/", StaffVerify.as_view(), name="staff_verify"),
    path("user-verify/", UserVerify.as_view(), name="user_verify"),
    path("user-verify/code-submit", UserCodeVerify.as_view(), name="user_code_verify"),
    path("user-verify/code-reset", UserVerify.as_view(), name="user_code_reset"),
    path("staff-verify/code-reset", StaffVerify.as_view(), name="staff_code_reset"),
    path(
        "staff-verify/code-submit", StaffCodeVerify.as_view(), name="staff_code_verify"
    ),
    path("user/account/", UserAcountView.as_view(), name="user_dashboard"),
    path("signup/", SignupPageView.as_view(), name="signup"),
    # path("login/1", CustomLoginView.as_view()),
]
