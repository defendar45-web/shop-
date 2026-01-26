from django.shortcuts import render, get_object_or_404
from products.models import Category, Product
from django.db.models import Q


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
    query = request.GET.get('q', '')
    products = []
    categories = []

    if query:
        query = query.strip()
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        categories = Category.objects.filter(
            name__icontains=query
        )

    return render(request, 'products/search.html', {
        'query': query,
        'products': products,
        'categories': categories,
    })


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)



