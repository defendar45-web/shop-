from django.contrib import admin
from brand.models import Brands


# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    ist_display = ('name',)
admin.site.register(Brands, BrandAdmin)
