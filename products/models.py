from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True)

    def get_image(self):
        return self.image.url

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    def get_image(self):
        return self.image.url

    def __str__(self):
        return self.name


class ProductCategory:
    objects = None