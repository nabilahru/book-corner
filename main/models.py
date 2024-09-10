from django.db import models

class DataProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    genre_category = models.CharField(max_length=255)
    quantity = models.IntegerField()
    description = models.TextField()
