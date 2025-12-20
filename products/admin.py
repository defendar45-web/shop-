from django.contrib import admin

from products.models import Category

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)