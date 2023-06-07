from django.db import models

from users.models import User


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    users = models.ManyToManyField(User, related_name='products')

    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
