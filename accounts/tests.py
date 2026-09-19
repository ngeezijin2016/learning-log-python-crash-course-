from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class RegisterViewTests(TestCase):
    def test_register_creates_new_user(self):
        response = self.client.post(
            reverse('accounts:register'),
            {
                'username': 'newuser',
                'password1': 'Testpass123!',
                'password2': 'Testpass123!',
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())
