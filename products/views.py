from django.shortcuts import render
from .models import *

def categories(request):
    return render(request, 'products/categories.html',{
        "categories":ProductCategory.objects.all()
    }
        )

def products(request):
    pass