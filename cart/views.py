from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from coupon.forms import AddCouponForm
from .forms import AddItemForm

from item.models import Item
from .models import Cart


@require_POST
def add(request, id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=id)

    #유효성 검사
    form = AddItemForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item, quantity=cd['quantity'], is_update=cd['is_update'])

    return redirect('cart:detail')

def remove(request, id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=id)
    cart.remove(item)
    return redirect('cart:detail')

def detail(request):
    cart = Cart(request)
    add_coupon = AddCouponForm()
    for cart_item in cart:
        cart_item['quantity_form'] = AddItemForm(initial={'quantity': cart_item['quantity'], 'is_update': True})
    return render(request, 'cart/cart_detail.html', {'cart':cart ,'add_coupon':add_coupon})