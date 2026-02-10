from django.shortcuts import render, get_object_or_404
from products.models import Category, Product
from django.db.models import Q
from users.models import Favorite


def categories(request):
    return render(request, 'products/categories.html',{
        "categories":Category.objects.all(),

    }
        )


def products_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category).order_by('-id')

    ## добавил  для добовление в изброное
    favorites = []

    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)


    return render(request, 'products/products_by_category.html',{
        "products":products,
        "category":category,
        "favorites":favorites,
    })

def search(request):
    query = request.GET.get('q', '')
    products = []
    categories = []
    favorites = []

    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)

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
        'favorites': favorites,
    })


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)



