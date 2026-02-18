

from django.db import models
from django.conf import settings
from django.db.models import Max

from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_order_number = models.PositiveIntegerField(blank=True, null=True)

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    floor = models.PositiveIntegerField()
    house_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)




    class Meta:
        unique_together = ('user', 'user_order_number')
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Если заказ создаётся впервые
        if not self.pk:
            last_number = Order.objects.filter(
                user=self.user
            ).aggregate(
                Max('user_order_number')
            )['user_order_number__max']

            self.user_order_number = 1 if last_number is None else last_number + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ №{self.user_order_number} пользователя {self.user.username}"


    def get_total_cost(self):
        return sum(item.get_total_price() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity


