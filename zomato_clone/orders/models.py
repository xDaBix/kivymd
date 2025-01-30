from django.db import models
from users.models import User
from restaurants.models import Restaurant

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.JSONField()  # Store ordered items as a JSON object
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ], default='pending')

    def __str__(self):
        return f"Order {self.id} by {self.user.username} at {self.restaurant.name}"