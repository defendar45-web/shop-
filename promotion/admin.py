from django.contrib import admin
from promotion.models import Promo


# Register your models here.
class PromoAdmin(admin.ModelAdmin):
    ist_display = ('name' 'date',)

admin.site.register(Promo, PromoAdmin)