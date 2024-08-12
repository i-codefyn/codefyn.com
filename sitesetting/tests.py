from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .models import (
    Brands,
    KeywordDiscription,
    Sites,
    Features,
    Faq,
    AboutCompany,
    SliderData,
    OurClients,
    GoogleFeeds,
)
from pages.models import OnlineRequest


class OnlineRequestTests(TestCase):
    def setUp(self):
        self.obj = OnlineRequest.objects.create(
            name="manish",
            email="manish@gmail.com",
            mobile="1234567890",
            device_name="fixenix",
            device_problem="broken",
        )
        url = reverse("online_requests_list")
        self.response = self.client.get(url)

    def test_ors__listing(self):
        self.assertEqual(f"{self.obj.name}", "manish")
        self.assertEqual(f"{self.obj.email}", "manish@gmail.com")
        self.assertEqual(f"{self.obj.mobile}", "1234567890")
        self.assertEqual(f"{self.obj.device_name}", "fixenix")
        self.assertEqual(f"{self.obj.device_problem}", "broken")


class GoogleFeedsTests(TestCase):
    def setUp(self):
        self.obj = GoogleFeeds.objects.create(
            google_feed="manish",
        )
        url = reverse("gf_list")
        self.response = self.client.get(url)

    def test_gf__listing(self):
        self.assertEqual(f"{self.obj.google_feed}", "manish")


class OurClientsTests(TestCase):
    def setUp(self):
        self.obj = OurClients.objects.create(
            name="manish",
            review="5",
        )
        url = reverse("oc_list")
        self.response = self.client.get(url)

    def test_oc__listing(self):
        self.assertEqual(f"{self.obj.name}", "manish")
        self.assertEqual(f"{self.obj.review}", "5")


class SliderDataTests(TestCase):
    def setUp(self):
        self.obj = SliderData.objects.create(
            heading1_title="manish h1",
            heading1="h1",
            heading2_title="manish h2",
            heading2="h2",
            heading3_title="manish h3",
            heading3="h3",
            heading4_title="manish h4",
            heading4="h4",
        )
        url = reverse("slider_list")
        self.response = self.client.get(url)

    def test_sliders__listing(self):
        self.assertEqual(f"{self.obj.heading1_title}", "manish h1")
        self.assertEqual(f"{self.obj.heading2_title}", "manish h2")
        self.assertEqual(f"{self.obj.heading3_title}", "manish h3")
        self.assertEqual(f"{self.obj.heading4_title}", "manish h4")
        self.assertEqual(f"{self.obj.heading1}", "h1")
        self.assertEqual(f"{self.obj.heading2}", "h2")
        self.assertEqual(f"{self.obj.heading3}", "h3")
        self.assertEqual(f"{self.obj.heading4}", "h4")


class AboutCompanyTests(TestCase):
    def setUp(self):
        self.obj = AboutCompany.objects.create(
            about_company="world best company manish",
        )
        url = reverse("faq_list")
        self.response = self.client.get(url)

    def test_about_company_listing(self):
        self.assertEqual(f"{self.obj. about_company}", "world best company manish")


class FaqTests(TestCase):
    def setUp(self):
        self.obj = Faq.objects.create(
            que="best developer in the world ? ",
            ans="manish",
        )
        url = reverse("faq_list")
        self.response = self.client.get(url)

    def test_faqs_listing(self):
        self.assertEqual(f"{self.obj.que}", "best developer in the world ? ")
        self.assertEqual(f"{self.obj.ans}", "manish")


class FeaturesTests(TestCase):
    def setUp(self):
        self.obj = Features.objects.create(
            main_title="manish",
            f1="www.manish.com",
            f2="www.manish.com",
            f3="www.manish.com",
            f4="www.manish.com",
            f5="www.manish.com",
            f6="www.manish.com",
            f1_title="www.manish.com",
            f2_title="www.manish.com",
            f3_title="www.manish.com",
            f4_title="www.manish.com",
            f5_title="www.manish.com",
            f6_title="www.manish.com",
        )
        url = reverse("feature_list")
        self.response = self.client.get(url)

    def test_faetures_listing(self):
        self.assertEqual(f"{self.obj.main_title}", "manish")
        self.assertEqual(f"{self.obj.f1}", "www.manish.com")
        self.assertEqual(f"{self.obj.f2}", "www.manish.com")
        self.assertEqual(f"{self.obj.f3}", "www.manish.com")
        self.assertEqual(f"{self.obj.f4}", "www.manish.com")
        self.assertEqual(f"{self.obj.f5}", "www.manish.com")
        self.assertEqual(f"{self.obj.f6}", "www.manish.com")
        self.assertEqual(f"{self.obj.f1_title}", "www.manish.com")
        self.assertEqual(f"{self.obj.f2_title}", "www.manish.com")
        self.assertEqual(f"{self.obj.f3_title}", "www.manish.com")
        self.assertEqual(f"{self.obj.f4_title}", "www.manish.com")
        self.assertEqual(f"{self.obj.f5_title}", "www.manish.com")
        self.assertEqual(f"{self.obj.f6_title}", "www.manish.com")


class SitesTests(TestCase):
    def setUp(self):
        self.obj = Sites.objects.create(
            domain_name="www.manish.com",
            display_name="www.manish.com",
            app_email="info@manish.com",
            app_mobile="1234567890",
            app_address="india",
            app_version="v5",
        )
        url = reverse("site_list")
        self.response = self.client.get(url)

    def test_sites_listing(self):
        self.assertEqual(f"{self.obj.domain_name}", "www.manish.com")
        self.assertEqual(f"{self.obj.display_name}", "www.manish.com")
        self.assertEqual(f"{self.obj.app_email}", "info@manish.com")
        self.assertEqual(f"{self.obj.app_mobile}", "1234567890")
        self.assertEqual(f"{self.obj.app_address}", "india")
        self.assertEqual(f"{self.obj.app_version}", "v5")


class KeywordsTests(TestCase):
    def setUp(self):
        self.obj = KeywordDiscription.objects.create(
            keyword="manish created this site",
            discription="manish",
        )
        url = reverse("keywords_list")
        self.response = self.client.get(url)

    def test_keys_listing(self):
        self.assertEqual(f"{self.obj.keyword}", "manish created this site")
        self.assertEqual(f"{self.obj.discription}", "manish")


class BrandTests(TestCase):
    def setUp(self):
        self.obj = Brands.objects.create(
            name="manish",
        )
        url = reverse("brand_list")
        self.response = self.client.get(url)

    def test_brand_listing(self):
        self.assertEqual(f"{self.obj.name}", "manish")


# Create your tests here.
