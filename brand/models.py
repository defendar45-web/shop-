from django.db import models

class Brands(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="brand/", null=True, blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return "/static/icons/no_image.png"