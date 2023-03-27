from django.shortcuts import render

# Create your views here.
from coinbase_commerce.client import Client
from django.shortcuts import render

from django.conf import settings


def home_view(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
        'local_price': {
            'amount': '0.50',
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'coinbase/payment/success/',
        'cancel_url': domain_url + 'coinbase/payment/cancel/',
    }
    charge = client.charge.create(**product)

    return render(request, 'home.html', {
        'charge': charge,
    })

def checkout(request):
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
        'local_price': {
            'amount': '0.50',
            'currency': 'USD'
        },
    }
    return  render(request, "Checkout.html", context={"checkout": product})

# payments/views.py

def success_view(request):
    return render(request, 'success.html', {})


def cancel_view(request):
    return render(request, 'cancel.html', {})
