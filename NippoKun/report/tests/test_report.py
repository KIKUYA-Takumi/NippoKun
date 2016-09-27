from django.test import TestCase, Client


# Create your tests here.


class CreateReportTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post('/report/user_register/',
                         {'username': 'john', 'password1': 'johnpass', 'password2': 'johnpass'})
        self.client.post('/report/login/', {'username': 'john', 'password': 'johnpass'})

    """
        status_code = 302: created new report.
        status_code = 200: not create new report.
    """

    def test_create_report(self):
        response = self.client.post('/report/report_entries/',
                                    {'report_title': 'test title', 'report_content': 'test'})
        self.assertEqual(response.status_code, 302)

    def test_create_report_no_report_title(self):
        response = self.client.post('/report/report_entries/',
                                    {'report_title': '', 'report_content': 'test'})
        self.assertEqual(response.status_code, 302)

    def test_create_report_no_report_content(self):
        response = self.client.post('/report/report_entries/',
                                    {'report_title': 'test title', 'report_content': ''})
        self.assertEqual(response.status_code, 302)

    def test_create_report_no_report_info(self):
        response = self.client.post('/report/report_entries/',
                                    {'report_title': '', 'report_content': ''})
        self.assertEqual(response.status_code, 302)


class UpdateReportTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post('/report/user_register/',
                         {'username': 'john', 'password1': 'johnpass', 'password2': 'johnpass'})
        self.client.post('/report/login/', {'username': 'john', 'password': 'johnpass'})

    """
        status_code = 404: deleted report.
        status_code = otherwise: not delete report.
    """

    def test_delete_report(self):
        report = self.client.post('/report/report_entries/',
                                  {'report_title': 'test title', 'report_content': 'test'})
        response = self.client.delete(report)
        self.assertEqual(response.status_code, 404)
