from django.shortcuts import render
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from orders.models import Order  # ваша модель заказа

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    amount = int(order.total_amount * 100)  # Stripe работает в центах

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': f'Заказ #{order.id}',
                },
                'unit_amount': amount,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
        metadata={
            'order_id': order.id
        }
    )
    return redirect(session.url, code=303)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = 'ваш_секретный_webhook'
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return JsonResponse({'status': 'invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'status': 'invalid signature'}, status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order_id = session['metadata']['order_id']
        order = Order.objects.get(id=order_id)
        order.is_paid = True
        order.save()

    return JsonResponse({'status': 'success'})
