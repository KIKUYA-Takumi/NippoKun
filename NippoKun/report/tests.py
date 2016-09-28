from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory

from .models import Report


# Create your tests here.


class UpdateReportTest(TestCase):
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
