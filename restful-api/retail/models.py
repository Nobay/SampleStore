from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.FloatField()


class Asset(models.Model):
    product = models.ForeignKey(Product, related_name='assets')
    image_url = models.URLField(max_length=500)


class Customer(User):
    """ Location employee model.  Foreign key to Store."""
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
