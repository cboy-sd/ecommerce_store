
from django.shortcuts import render
from .forms import OrderForm, ImageForm
from basket.basket import Basket
from .models import Order, OrderItem
import phonenumbers


def add(request):
    owner = request.user
    print(owner)
    basket = Basket(request)
    total_price = request.POST.get('total_price')
    print(total_price)
    if request.method == "POST":
        data = OrderForm(request.POST)
        if data.is_valid() :
            full_name = data.cleaned_data['full_name']
            phone = data.cleaned_data['phone']
            address = data.cleaned_data['address']
            email = data.cleaned_data['email']
            city = data.cleaned_data['city']
            if Order.objects.all().filter(user=owner, Done=False).exists():
                message = "you already have on pending please order after you order get Done "
                context = {
                    "message": message
                }

                return render(request, "order/feed_back.html", context)
            else:
                order = Order.objects.create(user=owner, full_name=full_name,
                                             phone=phone, total_price=total_price,
                                             address=address, email=email,
                                             city=city)
                order_id = order.pk
                context = {

                    "order_key": order.order_key
                }
                for item in basket:
                    OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'],
                                             quantity=item['qty'])
                    print(item['product'])
                basket.clear()
                return render(request, "payment/upload_attachment.html", context)
        else:
            context = {
                "basket": basket
            }
            return render(request, "payment/order_form.html", context)


def upload_invoice(request):
    if request.method == 'POST':
        order_key = request.POST.get("order_key")
        user = request.user
        if len(request.FILES) != 0:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                invo = form.cleaned_data['invoice']
                order =  Order.objects.get(order_key=order_key)
                order.invoice=invo
                order.billing_status=True
                order.save()
                print("order image uploaded")
                return render(request, "payment/orderplaced.html")
            else:
                return render(request, "payment/upload_attachment.html", {"order_key": order_key})
        else:
            return render(request, "payment/upload_attachment.html", {"order_key": order_key})


    # check if attachment file is not empty

    #         order = Order.objects.filter(order_key=order_key, user=user).update(
    #             invoice=invo, billing_status=True)
    #         order.save()
    #         return render(request, "payment/orderplaced.html")
    #     except:
    #         print("its not image file ")
    #         return render(request, "payment/upload_attachment.html", {"order_key": order_key})
    # else:
    #     print("files is empty")
    #     print(order_key)
    #     return render(request, "payment/upload_attachment.html", {"order_key": order_key})


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders