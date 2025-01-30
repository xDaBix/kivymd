from django.test import TestCase
from .models import Restaurant

class RestaurantModelTest(TestCase):

    def setUp(self):
        Restaurant.objects.create(name="Test Restaurant", location="Test Location", cuisine_type="Italian", rating=4.5)

    def test_restaurant_creation(self):
        restaurant = Restaurant.objects.get(name="Test Restaurant")
        self.assertEqual(restaurant.location, "Test Location")
        self.assertEqual(restaurant.cuisine_type, "Italian")
        self.assertEqual(restaurant.rating, 4.5)

class RestaurantViewTest(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(name="Test Restaurant", location="Test Location", cuisine_type="Italian", rating=4.5)

    def test_restaurant_list_view(self):
        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")

    def test_restaurant_detail_view(self):
        response = self.client.get(f'/restaurants/{self.restaurant.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")