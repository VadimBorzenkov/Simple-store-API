from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.PositiveIntegerField()
