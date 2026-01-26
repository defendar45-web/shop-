from django.shortcuts import render, get_object_or_404
from products.models import Category, Product, ProductCategory


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

def search(request):
    query = request.GET.get('q')
    products = []
    categories = []

    if query:
        products = Product.objects.filter(name__icontains=query)


    return render(request, 'products/search.html', {
        'query': query,
        'products': products,

    })


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)



