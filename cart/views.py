from cart.models import CartItem
from django.shortcuts import render


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    subtotal = sum(item.get_total_price() for item in cart_items)
    total_price = subtotal
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total_price': total_price,
    })





