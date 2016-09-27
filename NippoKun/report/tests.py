from django.test import TestCase, Client


# Create your tests here.


class ClientTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.post('/report/login/')
        self.assertEqual(response.status_code, 500)

    def test_mypage(self):
        response = self.client.get('/report/mypage/')
        self.assertEqual(response.status_code, 302)

    def test_index(self):
        response = self.client.get('/report/index/')
        self.assertEqual(response.status_code, 302)

    def test_search(self):
        response = self.client.get('/report/search/')
        self.assertEqual(response.status_code, 302)

    def test_user_register(self):
        response = self.client.get('/report/user_register/')
        self.assertEqual(response.status_code, 200)
