import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Services(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_name = models.CharField(max_length=100)
    service_for = models.CharField(max_length=100)
    service_price = models.DecimalField(max_digits=6, decimal_places=2)
    bg_cover = models.ImageField(upload_to="services/", blank=True)

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):  # new
        return reverse("service_detail", args=[str(self.id)])


class Reviews(models.Model):
    services = models.ForeignKey(
        Services,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
