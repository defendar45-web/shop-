from django.contrib import admin

from .models import Seminars


# Register your models here.
class SeminarsAdmin(admin.ModelAdmin):
    ist_display = ('name' 'date',)

admin.site.register(Seminars ,SeminarsAdmin)
