from django.shortcuts import render, reverse
from .forms import *
from .models import OrderItem
from basket.basket import Basket
from .models import Order, OrderItem
from django.db import transaction


def add(request):
    basket = Basket(request)
    attachment = "payment/upload_attachment.html"
    data = dict(request.itmes())
    if request.user.is_authenticated:
        order_data = {
            "full_name": data.get('full_name'),
            "email": data.get('email'),
            "phone": data.get('phone'),
            "net_total": data.get('net_total'),
        }
        form = OrderForm(order_data)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()
                for item in basket:
                    order_item = OrderItem.objects.create(
                        product=item['product'],
                        price=item['price'],
                        quantity=item['qnt'],
                        order=order.pk
                    )
                basket = basket.clear()
                print(basket)
                return render(request, attachment, {"order_id": order.pk})
        return render("payment/order_form.html", {"basket": basket})

    return render(request, "payment/order_form.html", )


def upload_invoice(request):
    if request.method == 'POST':
        order_id = request.POST.get("order_id")
        user = request.user
        form = OrderAttachmentForm(request.POST, request.FILES)
        if len(request.FILES) != 0 and form.is_valid():
            form.billing_status = True
            form.save()
            return render(request, "payment/orderplaced.html")

    return render(request, "payment/upload_attachment.html", {"order_id": order_id})


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
