
from django.db.models import Model
from django.db import models
from django.utils import timezone


class Seminars(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="courses/", null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def get_image(self):
        if self.image:
            return self.image.url
        return "/static/icons/no_image.png"

