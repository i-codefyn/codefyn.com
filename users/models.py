from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from django.urls import reverse



class CustomUser(AbstractUser):
     
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     pass

     def __str__(self):
        return self.username

     def get_absolute_url(self): # new
        return reverse('users', args=[str(self.id)])
     
