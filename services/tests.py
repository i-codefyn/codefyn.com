from django.test import client, TestCase
from django.urls import reverse, resolve
from .models import Services, Reviews
from .views import MobileAndTabServices, ComputerLaptopServices
from django.contrib.auth import get_user_model


class ComputerLaptopTests(TestCase):
    def setUp(self):
        url = reverse("computer_laptop_services")
        self.response = self.client.get(url)

    def test_computerlaptop_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home/computer_services.html")
        self.assertContains(self.response, "Our Computer And Laptop Related Services")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_computerlaptop_view(self):  # new
        view = resolve("/services/ComputerLaptop/")
        self.assertEqual(view.func.__name__, ComputerLaptopServices.as_view().__name__)


class MobileandTabTests(TestCase):
    def setUp(self):
        url = reverse("mobile_tab_services")
        self.response = self.client.get(url)

    def test_mobiletab_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "home/mobile_services.html")
        self.assertContains(self.response, "Our Mobile And Tab Related Services")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_mobiletab_view(self):  # new
        view = resolve("/services/mobileTab/")
        self.assertEqual(view.func.__name__, MobileAndTabServices.as_view().__name__)


class ServicesTest(TestCase):
    def setUp(self):
        url = reverse("services")
        self.response = self.client.get(url)
        self.user = get_user_model().objects.create_user(  # new
            username="reviewuser", email="reviewuser@email.com", password="testpass123"
        )

        self.services = Services.objects.create(
            service_name="doorstep for mobile",
            service_for="mobile",
            service_price="150.00",
        )
        self.review = Reviews.objects.create(
            services=self.services, author=self.user, review="an exceent services"
        )

    def test_services_listing(self):
        self.assertEqual(f"{self.services.service_name}", "doorstep for mobile")
        self.assertEqual(f"{self.services.service_for}", "mobile")
        self.assertEqual(f"{self.services.service_price}", "150.00")
        self.assertEqual(f"{self.review.review}", "an exceent services")

    def test_services_list_view(self):
        response = self.client.get(reverse("services"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "mobile")
        self.assertTemplateUsed(response, "services/service_list.html")

    def test_services_detail_view(self):
        response = self.client.get(self.services.get_absolute_url())
        no_response = self.client.get("services/12345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "mobile")
        self.assertTemplateUsed(response, "services/service_details.html")
