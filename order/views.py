
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from common.forms import MemberForm
from order.forms import OrderForm
from django.db.models import F
from order.models import OrderItem, Order
from django.shortcuts import render, redirect


@login_required(login_url='/login/')
def order_create(request):
    cart = Cart(request)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.email = request.user

            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount

                order.save()


            for cart_item in cart:
                OrderItem.objects.create(order=order, item=cart_item['item'], price=cart_item['item_price'], quantity=cart_item['quantity'])

            cart.clear()



            return render(request, 'order/complete.html', {'order': order})

    else:
        form = OrderForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})


def order_complete(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)

    for order_item in order.items.all():
        item = order_item.item

        item.sales = F('sales') + order_item.quantity  # 판매량 증가
        item.save()

    return render(request, 'order/complete.html', {'order':order})




def order_form(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.email = request.user
            member.save()
            return redirect('order:order_create')
    else:
        form = MemberForm()

    context = {'form': form}
    return render(request, 'order/create.html', context)