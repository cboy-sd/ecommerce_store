
from django.http import response
from django.shortcuts import render, redirect, get_object_or_404, reverse
from orders.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from account.models import UserBase
from store.models import Product

@login_required()
def dashboard_view(request):
    users = UserBase.objects.all().count()
    earnings = Order.objects.all()
    total_funds = 0
    for funds in earnings:
        total_funds = total_funds + funds.total_price
    print(total_funds)
    items = OrderItem.objects.all()
    sales = 0
    for item in items:
        sales += item.quantity
    print(f'all sales are {sales}')
    incomplete_orders = Order.objects.filter(billing_status=False, Done=False).count()
    order_succeded = Order.objects.filter(billing_status=True, Done=True).count()
    orders_on_pend = Order.objects.filter(billing_status=True, Done=False).count()
    print(f' succeeded_orders{order_succeded}')
    print(incomplete_orders)
    products = Product.objects.all().count()

    total_orders = Order.objects.all().count()
    print(f'all the orders are:{total_orders}')
    context = {
        "total_funds": total_funds,
        "sales": sales,
        "incomplete_order": incomplete_orders,
        "order_succeded": order_succeded,
        "order_on_pend": orders_on_pend,
        "users": users,
        "orders": total_orders,
        "products": products,
    }
    return render(request, "admin/admin_dashboard.html", context)


def admin_orders_dashboard_views(request):
    orders = Order.objects.all()
    orders_items = OrderItem.objects.all()
    context = {
        "orders_items": orders_items,
        "orders": orders
    }

    return render(request, "admin/manage_orders.html", context)


def order_update(request):
    user = request.user
    if user.is_staff:
        order_key = request.order_ke


def product_manage(request):
    if request.user.is_staff:
        products = Product.objects.all()
        context = {
            "products": products,

        }
        return render(request, "admin/manage.orders.html")


@login_required
def order_detail_view(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)
    items = OrderItem.objects.filter(order=id).all()
    print()
    context = {
        "order": order,
        "items": items

    }
    return render(request, "admin/detail.html", context)


def order_delete_view(request):
    id = request.POST.get('id')
    order_id  = str(id)
    user = request.user
    order = Order.objects.get(id=order_id, user=user)
    order.delete()
    print(order.user)
    return redirect('/')


def order_reject_view(request):
    id = request.POST.get('id')
    order_id  = str(id)
    user = request.user
    order = Order.objects.get(id=order_id, user=user)
    order.status = "Rejected"
    order.Done = False
    order.save()
    print(order.status)
    return redirect('/')


def order_accept_view(request):
    id = request.POST.get('id')
    order_id = str(id)
    user = request.user
    order = Order.objects.get(id=order_id, user=user)
    order.status = "Accepted"
    order.save()
    print(f'your order is {order.status}')
    return redirect('/')

def order_fulfilled_view(request):
    id = request.POST.get('id')
    order_id = str(id)
    user = request.user
    order = Order.objects.get(id=order_id, user=user)
    order.Done = True
    order.save()
    print(f'your order is {order.Done}')
    return redirect('/')

def order_unfulfilled_view(request):
    id = request.POST.get('id')
    order_id = str(id)
    user = request.user
    order = Order.objects.get(id=order_id, user=user)
    order.Done = False
    order.save()
    print(f'your order is not done and its  {order.Done}')
    return redirect('/')

from django.shortcuts import render

# Create your views here.