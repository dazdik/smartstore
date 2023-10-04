from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/index.html')


class ProductListViewTestCase(TestCase):
    fixtures = ['categories.json', 'books.json']

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_tests(response)
        self.assertQuerysetEqual(response.context_data.get('object_list'), self.products.all()[:3], ordered=False)

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertQuerysetEqual(response.context_data.get('object_list'),
                                 self.products.filter(category_id=category.id), ordered=False)

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
