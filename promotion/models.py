from django.db import models


class Promo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="promo/", null=True, blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return "/static/icons/no_image.png"

