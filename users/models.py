from django.contrib.auth.models import AbstractUser
from django.db import models

from products.models import Product


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # ❗ нельзя добавить дважды

    def __str__(self):
        return f'{self.user} ❤️ {self.product}'