from django.test import TestCase
from django.urls import reverse

from .models import Menu

# Create your tests here.    

class MenuModelTest(TestCase):    
    
    def setUp(self):
        self.data = Menu.objects.create(name='test name', price=10, description='test description')

    def test_menu_model_entry(self):
        """
        Test Menu model data insertion/types/field attributes
        """
        data = self.data
        self.assertTrue(isinstance(data, Menu))
        self.assertEqual(str(data), 'test name')
        self.assertEqual(data.description, 'test description')
        self.assertEqual(data.price, 10)

    def test_menu_url(self):
        """
        Test menu model URL reverse
        """
        data = self.data
        response = self.client.post(reverse('menu'))
        self.assertEqual(response.status_code, 200)

class MenuViewTest(TestCase):    
    
    def setUp(self):
        self.data = Menu.objects.create(name='test name', price=10, description='test description')

    def test_menu(self):
        data = self.data
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
