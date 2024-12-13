from django.db import models

#from address.models import AddressField

# Create your models here.

class PropertyType(models.TextChoices):
    DUPLEX = 'd', 'duplex'
    APARTMENT = 'a', 'apartment'
    LAND = 'l', 'land'

class PaymentType(models.TextChoices):
    BUY = 'b', 'buy'
    RENT = 'r', 'rent'

class Property(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False) 
    propertyType = models.CharField(
            max_length=1,
            choices=PropertyType.choices,
            default=None
    )
    price = models.FloatField()
    paymentType = models.CharField(
            max_length=1,
            choices=PaymentType.choices,
            default=None
    )
    bedrooms = models.SmallIntegerField()
    bathrooms = models.SmallIntegerField()
    sizeW = models.SmallIntegerField(null=False, blank=False)
    sizeB = models.SmallIntegerField(null=False, blank=False)
    available = models.BooleanField(default=False, null=False, blank=False)
