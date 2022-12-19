from django.forms import forms
from .models import Order, OrderAttachment


class OrderForm(forms.Form):
    class Meta:
        model = Order
        exclude = [
            'billing_status',
            'created',
            'updated',
        ]


class OrderAttachmentForm(forms.Form):
    class Meta:
        model = OrderAttachment
        exclude = [
            'created',
            'updated',
        ]
