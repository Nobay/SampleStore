from enum import Enum, IntEnum

from django.contrib.auth.models import User
from django.db import models

UserStatus = (
    ('0', 'New'),
    ('1', 'Active'),
    ('2', 'Blocked'),
    ('3', 'Banned')
)


OrderStatus = (
    ('0', 'New'),
    ('1', 'Hold'),
    ('2', 'Shipped'),
    ('3', 'Delivered'),
    ('4', 'Closed')
)


class Category(models.Model):
    """ Category model"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


class Product(models.Model):
    """ Product model. Foreign key to Category"""
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.FloatField()


class Asset(models.Model):
    product = models.ForeignKey(Product)
    image_url = models.URLField(max_length=500)


class Customer(User):
    """ Location employee model.  Foreign key to Store."""
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
