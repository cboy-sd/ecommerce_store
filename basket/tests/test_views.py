from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Product, Category

from django.urls import reverse


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django intermediate', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')

        self.client.postt(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True
        )
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "prodcutqty": 2, "action": "post"}, xhr=True)


    def test_basket_url(self):
        """
        Test home page state response
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)
