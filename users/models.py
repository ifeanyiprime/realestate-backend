from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    CLIENT = 'c', 'client'
    AGENT = 'a', 'agent'

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    #profile_img = models.ImageField(upload_to="profiles", null=True, blank=True)
    realtor = models.BooleanField(default=False, blank=True, null=False)
    role = models.CharField(
            max_length=1,
            choices=Role.choices,
            default='c'
    )


