from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=255, decimal_places=2)
    ingredients = models.TextField(max_length=255)
    category = models.CharField(max_length=50)
    stock = models.PositiveSmallIntegerField()
    discount = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"
    