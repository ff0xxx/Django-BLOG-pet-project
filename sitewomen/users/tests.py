from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class RegisterUserTestCase(TestCase):
    def setUp(self):
        pass

    def test_form_registration_get(self):
        path = reverse('users:register')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_success(self):
        data = {
            'username': 'user_1',
            'email': 'user1@sitewomen.ru',
            'first_name': 'Sergey',
            'last_name': 'Balakirev',
            'password1': '12345678Aa',
            'password2': '12345678Aa',
        }

        user_model = get_user_model()

        path = reverse('users:register')
        response = self.client.post(path, data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(user_model.objects.filter(username=data['username']).exists())
