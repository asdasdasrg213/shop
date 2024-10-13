from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='images/')
    brand = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    guarantee = models.CharField(max_length=30)
    discount = models.PositiveSmallIntegerField()
    raiting = models.FloatField()
    stock = models.PositiveIntegerField()