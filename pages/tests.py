from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .form import FeedBackForm, ContactForm, OnlineRequestForm
from .views import (
    HomePageView,
    ContactFormView,
    FeedBackFormView,
    DisclamerView,
    FaqsView,
    AboutUs,
)
from .models import OnlineRequest, FeedBack, ContactUs


class AboutUsTests(TestCase):
    def setUp(self):
        url = reverse("aboutus")
        self.response = self.client.get(url)

    def test_aboutus_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home/about_us.html")
        self.assertContains(self.response, "About Us")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_aboutus_view(self):  # new
        view = resolve("/aboutus/")
        self.assertEqual(view.func.__name__, AboutUs.as_view().__name__)


class FaqsTests(TestCase):
    def setUp(self):
        url = reverse("faqs")
        self.response = self.client.get(url)

    def test_faqs_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home/faqs.html")
        self.assertContains(self.response, "FAQ's")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_faqs_view(self):  # new
        view = resolve("/faqs/")
        self.assertEqual(view.func.__name__, FaqsView.as_view().__name__)


class HomePageTests(TestCase):
    def setUp(self):
        self.ors = OnlineRequest.objects.create(
            name="manish",
            email="manish@gmail.com",
            mobile="1234567890",
            device_name="One Plus",
            device_problem="Display",
        )
        url = reverse("Home")
        self.response = self.client.get(url)

    def test_homepage_listing(self):
        self.assertEqual(f"{self.ors.name}", "manish")
        self.assertEqual(f"{self.ors.email}", "manish@gmail.com")
        self.assertEqual(f"{self.ors.mobile}", "1234567890")
        self.assertEqual(f"{self.ors.device_name}", "One Plus")
        self.assertEqual(f"{self.ors.device_problem}", "Display")

    def test_homepage_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home/index.html")
        self.assertContains(self.response, "Get Free Quote")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_form(self):
        form = self.response.context.get("enquiryform")
        self.assertIsInstance(form, OnlineRequestForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_homepage_view(self):  # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class DisclaimerTests(TestCase):
    def setUp(self):
        url = reverse("disclamer")
        self.response = self.client.get(url)

    def test_disclamer_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home/Disclamer.html")
        self.assertContains(self.response, "Disclaimer")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_disclamer_view(self):  # new
        view = resolve("/disclamer/")
        self.assertEqual(view.func.__name__, DisclamerView.as_view().__name__)


class FeedbackTests(TestCase):  # new
    def setUp(self):
        url = reverse("feedback")
        self.response = self.client.get(url)
        self.fb = FeedBack.objects.create(
            email="manish@gmail.com",
            rating="5",
        )

    def test_feedback_listing(self):
        self.assertEqual(f"{self.fb.rating}", "5")
        self.assertEqual(f"{self.fb.email}", "manish@gmail.com")

    def test_feedback_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home/feedback.html")
        self.assertContains(self.response, "Feedback")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_feedback_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, FeedBackForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_feedback_view(self):  # new
        view = resolve("/feedback/")
        self.assertEqual(view.func.__name__, FeedBackFormView.as_view().__name__)


class ContactFormTests(TestCase):
    def setUp(self):
        url = reverse("contactus")
        self.response = self.client.get(url)
        self.cf = ContactUs.objects.create(
            name="manish",
            email="manish@gmail.com",
            message="Hi There",
        )

    def test_contactform_listing(self):
        self.assertEqual(f"{self.cf.name}", "manish")
        self.assertEqual(f"{self.cf.email}", "manish@gmail.com")
        self.assertEqual(f"{self.cf.message}", "Hi There")

    def test_contactform_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home/contact_us.html")
        self.assertContains(self.response, "Contact Form")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_contactform_form(self):
        form = self.response.context.get("form_contact")
        self.assertIsInstance(form, ContactForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_contactform_view(self):  # new
        view = resolve("/contactus/")
        self.assertEqual(view.func.__name__, ContactFormView.as_view().__name__)
