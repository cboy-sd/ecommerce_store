from unittest import skip

from django.test import TestCase, RequestFactory, Client
from store.models import Product, Category
from store.views import product_detail, all_products
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User


# @skip("skip demo statring")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViews(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')

    def test_allowed_hosts(self):
        """ test that url is responsive """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        print(f' your request massage is  http_{response.status_code}_ok')

    def test_product_detail_url(self):
        """ 
        test that the test is returning url correct
        """""
        response = self.c.get(reverse("store:product_detail", args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_url(self):
        """ test that category  url is the functioning"""
        res = self.c.get(reverse("store:category_list", args=['django']))
        self.assertEqual(res.status_code, 200)

    def test_home_page_template(self):
        """ tes that html """
        request = HttpResponse()
        response = all_products(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.__contains__("Africano Store"))
        # print(html)
        self.assertTrue(html)

    def test_view_function(self):
        request = self.factory.get("/django-beginners")
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertTrue(html)

    def test_url_allowed_hosts(self):


        response1 = self.c.get('/', HTTP_HOST='mohammedafricano.com')
        self.assertEqual(response1.status_code, 400)
        response = self.c.get('/', HTTP_HOST='mohammedafricano.com')
        self.assertEqual(response.status_code, 200)
