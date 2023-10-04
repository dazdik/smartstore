from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.forms import UserRegistrationForm
from users.models import EmailVerification, User


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'username': 'ivan2023',
            'email': 'ivanivanov90@example.com',
            'password1': '12345678aS',
            'password2': '12345678aS',
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/registration.html')
        self.assertIsInstance(response.context['form'], UserRegistrationForm)

    def test_user_registration_post_success(self):

        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        # check creating user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response.url, '/users/login/')
        self.assertTrue(User.objects.filter(username=username).exists())

        # check email verification
        email_verifications = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verifications.exists())
        self.assertEqual(email_verifications.first().expiration.date(), (now() + timedelta(hours=48)).date())

    def test_user_registration_post_error(self):
        User.objects.create(
            username=self.data['username'],
            email=self.data['email'],
        )
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
