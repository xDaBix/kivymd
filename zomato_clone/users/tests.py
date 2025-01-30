from django.test import TestCase
from django.urls import reverse
from .models import User

class UserModelTests(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))

class UserViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_register_view(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')  # Check if username is in the profile page