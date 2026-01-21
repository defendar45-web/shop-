from django.shortcuts import render

from cart.models import CartItem
from orders.models import Order, OrderItem


def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if request.method == "POST":
        name = request.POST['name']
        city = request.POST['city']
        street = request.POST['street']
        house_number = request.POST['house_number']
        floor = request.POST['floor']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        order = Order.objects.create(
            user=request.user,
            name=name,
            city=city,
            street=street,
            house_number=house_number,
            floor=floor,
            phone_number=phone_number,
            email=email,
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        cart_items.delete()
        return render(request, "orders/order_success.html", {
            "order": order,
        })



    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, "orders/checkout.html", {
        "cart_items": cart_items,
        "total_price": total_price
    })