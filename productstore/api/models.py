from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url = models.URLField()
    price = models.CharField(max_length=255)
    mrp = models.CharField(max_length=255)
    description = models.TextField()
    Fit = models.CharField(max_length=255)
    Fabric = models.CharField(max_length=255)
    Neck = models.CharField(max_length=255)
    Sleeve = models.CharField(max_length=255)
    Pattern = models.CharField(max_length=255)
    Length = models.CharField(max_length=255)
    def __str__(self):
        return self.name

