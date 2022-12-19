import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from basket.basket import Basket


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')



class Error(TemplateView):
    template_name = 'payment/error.html'


@login_required
def BasketView(request):
    basket = Basket(request)
    print(basket)
    total = basket.get_subtotal_price()
    print(total)
    context = {
        "total_price": total,
        "basket": basket
    }
    return render(request, 'payment/order_form.html', context)

