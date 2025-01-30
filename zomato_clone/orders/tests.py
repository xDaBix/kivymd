from django.test import TestCase
from .models import Order

class OrderModelTest(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            user_id=1,
            restaurant_id=1,
            total_amount=25.00,
            status='Pending'
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user_id, 1)
        self.assertEqual(self.order.restaurant_id, 1)
        self.assertEqual(self.order.total_amount, 25.00)
        self.assertEqual(self.order.status, 'Pending')

    def test_order_string_representation(self):
        self.assertEqual(str(self.order), f'Order {self.order.id} - {self.order.status}')