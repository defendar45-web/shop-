from django.db import models
from django.shortcuts import get_object_or_404, render


class Promo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="promo/", null=True, blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        return "/static/icons/no_image.png"

def promo_image(request, promo_id):
    promo = get_object_or_404(Promo, id=promo_id)
    return render(request, 'promotion/promo_image.html', {'promo': promo})