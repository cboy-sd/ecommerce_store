from django.test import TestCase
from store.models import Product, Category
from django.contrib.auth.models import User
from django.urls import reverse



class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='electronics', slug='electronics')

    def test_category_model_entry(self):
        """test and sure that the category"""
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'electronics')


class TestProductModel(TestCase):
    """testinig the product model"""

    def setUp(self):
        self.data1 = Category.objects.create(name='electronics', slug='electronics')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')
        self.data2 = Product.products.create(category_id=1, title='django advanced', created_by_id=1,
                                             slug='django-advanced', price='20.00', image='django', is_active=False)

    def test_product_model_entry(self):
        """test that product model insertion/types fields and a tributes"""

        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data.title), 'django beginners')


    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data = self.data1
        url = reverse('store:product_detail', args=[data.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:product_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

