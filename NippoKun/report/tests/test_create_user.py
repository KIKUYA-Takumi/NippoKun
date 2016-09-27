from django.contrib.auth.models import User
from django.test import TestCase, Client


class CreateUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_count = User.objects.count()

    """
        status_code = 302: created new user.
        status_code = 200: not create new user.
    """

    def test_create_user(self):
        response = self.client.post('/report/user_register/',
                                    {'username': 'john', 'password1': 'johnpass', 'password2': 'johnpass'})
        self.assertEqual(response.status_code, 302)

    def test_create_user_no_username(self):
        response = self.client.post('/report/user_register/',
                                    {'username': '', 'password1': 'johnpass', 'password2': 'johnpass'})
        self.assertEqual(response.status_code, 302)

    def test_create_user_no_password(self):
        response = self.client.post('/report/user_register/',
                                    {'username': 'john', 'password1': '', 'password2': ''})
        self.assertEqual(response.status_code, 302)

    def test_create_user_no_password1(self):
        response = self.client.post('/report/user_register/',
                                    {'username': 'john', 'password1': '', 'password2': 'johnpass'})
        self.assertEqual(response.status_code, 302)

    def test_create_user_no_password2(self):
        response = self.client.post('/report/user_register/',
                                    {'username': 'john', 'password1': 'johnpass', 'password2': ''})
        self.assertEqual(response.status_code, 302)

    def test_create_user_no_info(self):
        response = self.client.post('/report/user_register/',
                                    {'username': '', 'password1': '', 'password2': ''})
        self.assertEqual(response.status_code, 302)
