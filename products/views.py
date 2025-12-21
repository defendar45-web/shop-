from django.shortcuts import render
from products.models import Category





def categories(request):
    return render(request, 'products/categories.html',{
        "categories":Category.objects.all(),

    }
        )

def products(request):
    pass