from django.shortcuts import render
from products.models import Category,  Product


def categories(request):
    return render(request, 'products/categories.html',{
        "categories":Category.objects.all(),

    }
        )

def products_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category).order_by('-id')

    return render(request, 'products/products_by_category.html',{
        "products":products,
        "category":category,
    })




