from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Gri1BCxskqFm91kRXpbis3zcR9vufj1JzC1AO8RPcqkbMsR8FngZy54rDPq1ycFZP5nkNvKRm1IvODCxw5pUaAV00UUj6Hlmj',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)