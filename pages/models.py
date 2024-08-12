from django.db import models
import uuid
from django.urls import reverse


class FeedBack(models.Model):
    """Feedback"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=50)
    rating = models.CharField(max_length=5)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("feedback", args=[str(self.id)])


class ContactUs(models.Model):
    """Contact form"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("msg", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Contact Us"


class OnlineRequest(models.Model):
    """Online Request Create Model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    # company_name = models.CharField(max_length=200)
    email = models.EmailField()
    # webtype = models.CharField(max_length=300)
    # packages = models.CharField(max_length=300)
    services = models.CharField(max_length=300)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("online_requests", args=[str(self.id)])
