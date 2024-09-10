from django.test import TestCase

from django.test import TestCase, Client
from .models import DataProduct

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_product_name_user(self):
        product = DataProduct.objects.create(
            name = "BUMI",
            price = 75000,
            genre_category = "Fantasy book",
            quantity = 10,
            description = "It's a book about trio friends, who wonder around fantasy world" 
        )
        self.assertTrue(product)