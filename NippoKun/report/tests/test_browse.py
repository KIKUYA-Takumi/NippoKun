from django.test import TestCase


class LoginTest(TestCase):
    def setUp(self):
        self.client.post('/report/user_register/',
                         {'username': 'john', 'password1': 'johnpass', 'password2': 'johnpass'})

    """
        status_code = 302: success login.
        status_code = 200: not success login.
    """

    def test_login(self):
        response = self.client.post('/report/login/', {'username': 'john', 'password': 'johnpass'})
        self.assertEqual(response.status_code, 302)

    def test_login_no_username(self):
        response = self.client.post('/report/login/', {'username': '', 'password': 'johnpass'})
        self.assertEqual(response.status_code, 302)

    def test_login_no_password(self):
        response = self.client.post('/report/login/', {'username': 'john', 'password': ''})
        self.assertEqual(response.status_code, 302)


class ClientTest(TestCase):
    def setUp(self):
        self.client.post('/report/user_register/',
                         {'username': 'john', 'password1': 'johnpass', 'password2': 'johnpass'})
        self.client.post('/report/login/', {'username': 'john', 'password': 'johnpas'})

    """
        status_code = 302: success transition page.
        status_code = 200: success logout.
    """

    def test_mypage(self):
        response = self.client.get('/report/mypage/')
        self.assertEqual(response.status_code, 302)

    def test_index_page(self):
        response = self.client.get('/report/index/')
        self.assertEqual(response.status_code, 302)

    def test_search_page(self):
        response = self.client.get('/report/search/')
        self.assertEqual(response.status_code, 302)

    def test_create_report_page(self):
        response = self.client.get('/report/report_entries/')
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        response = self.client.get('/report/logout/')
        self.assertEqual(response.status_code, 200)
