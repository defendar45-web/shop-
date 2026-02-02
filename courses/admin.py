from django.contrib import admin

from .models import Seminars



class SeminarsAdmin(admin.ModelAdmin):
    ist_display = ('name' 'date',)

admin.site.register(Seminars ,SeminarsAdmin)
