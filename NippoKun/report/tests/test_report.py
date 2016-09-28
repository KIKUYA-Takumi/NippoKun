from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory

from ..models import Report


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


class DeleteReportTest(TestCase):
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


class UpdateReportContentTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post('/report/user_register/',
                         {'username': 'john',
                          'password1': 'johnpass',
                          'password2': 'johnpass'})
        self.client.login(username='john', password='johnpass')
        request_factory = RequestFactory()
        self.request = request_factory.get('/report/mypage/')

    def test_update_report_content(self):
        self.request.user = User.objects.get(pk=1)
        self.client.post('/report/report_entries/',
                         {'report_author': self.request.user,
                          'report_title': 'test title',
                          'report_content': 'test'
                          })
        self.request.report = Report.objects.get(pk=1)
        report = {
            'report_author': self.request.report.report_author,
            'report_title': self.request.report.report_title,
            'report_content': 'update content'
        }
        self.client.post('/report/1/edition/', report)
        self.request.report = Report.objects.get(pk=1)
        self.assertEqual(self.request.report.report_content, 'update content')


class UpdateReportTitleTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post('/report/user_register/',
                         {'username': 'john',
                          'password1': 'johnpass',
                          'password2': 'johnpass'})
        self.client.login(username='john', password='johnpass')
        request_factory = RequestFactory()
        self.request = request_factory.get('/report/mypage/')

    def test_update_report_title(self):
        self.request.user = User.objects.get(pk=1)
        self.client.post('/report/report_entries/',
                         {'report_author': self.request.user,
                          'report_title': 'test title',
                          'report_content': 'test'
                          })
        self.request.report = Report.objects.get(pk=1)
        report = {
            'report_author': self.request.report.report_author,
            'report_title': 'update title',
            'report_content': self.request.report.report_content
        }
        self.client.post('/report/1/edition/', report)
        self.request.report = Report.objects.get(pk=1)
        self.assertEqual(self.request.report.report_title, 'update title')
