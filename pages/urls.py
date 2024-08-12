from django.urls import path

from pages.views import (
    HomePageView,
    AboutUs,
    FaqsView,
    TermsAndConditionsView,
    DisclamerView,
    OtpVerify,
    FeedBackFormView,
    SendHTMLMail,
    OtpReset,
    ContactFormView,
    OurWorks,
    ProjectDiscussFormView,
    PrivacyPolicyView,
    RefundPolicyView,
    LatestDesignsView,

)

app_name = "Home"
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("latest-designs", LatestDesignsView.as_view(), name="latest_designs"),
    path("privacy-policy/", PrivacyPolicyView.as_view(), name="privacy_policy"),
    path("refund-policy/", RefundPolicyView.as_view(), name="refund_policy"),
    path("project-discuss/", ProjectDiscussFormView.as_view(), name="project_discuss"),
    path("works", OurWorks.as_view(), name="works"),
    path("otp-verify/", OtpVerify.as_view(), name="otp_verify"),
    path("otp-resend/", OtpReset, name="otp_reset"),
    path("aboutus/", AboutUs.as_view(), name="aboutus"),
    path("contactus/", ContactFormView.as_view(), name="contactus"),
    path("feedback/", FeedBackFormView.as_view(), name="feedback"),
    path("faqs/", FaqsView.as_view(), name="faqs"),
    path("disclamer/", DisclamerView.as_view(), name="disclamer"),
    path(
        "terms-conditions/",
        TermsAndConditionsView.as_view(),
        name="terms_and_conditions",
    ),  # new
]
