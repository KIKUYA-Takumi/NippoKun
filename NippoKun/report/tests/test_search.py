from django.contrib.auth.models import User
from django.db.models import Q
from django.test import TestCase, Client, RequestFactory

from ..models import Report


# Create your tests here.


class SearchTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post('/report/user_register/',
                         {'username': 'john',
                          'password1': 'johnpass',
                          'password2': 'johnpass'})
        self.client.login(username='john', password='johnpass')
        request_factory = RequestFactory()
        self.request = request_factory.get('/report/mypage/')
        self.request.user = User.objects.get(pk=1)
        self.client.post('/report/report_entries/',
                         {'report_author': self.request.user,
                          'report_title': 'test title',
                          'report_content': 'test'
                          })
        self.client.post('/report/report_entries/',
                         {'report_author': self.request.user,
                          'report_title': 'search test',
                          'report_content': 'search'
                          })

    def test_search_one_word(self):
        query_search_word = 'search'
        search_words = query_search_word.split()
        search_reports = []
        for i in range(len(search_words)):
            search_reports += Report.objects.filter(Q(report_content__contains=search_words[i]))
        count = len(search_reports)
        self.assertEqual(count, 1)

    def test_search_many_words(self):
        query_search_word = 'test search'
        search_words = query_search_word.split()
        search_reports = []
        for i in range(len(search_words)):
            search_reports += Report.objects.filter(Q(report_content__contains=search_words[i]))
        count = len(search_reports)
        self.assertEqual(count, 2)

    def test_search_no_hit_word(self):
        query_search_word = 'python'
        search_words = query_search_word.split()
        search_reports = []
        for i in range(len(search_words)):
            search_reports += Report.objects.filter(Q(report_content__contains=search_words[i]))
        count = len(search_reports)
        self.assertEqual(count, 0)


class SearchReportsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post('/report/user_register/',
                         {'username': 'john',
                          'password1': 'johnpass',
                          'password2': 'johnpass'})
        self.client.login(username='john', password='johnpass')
        request_factory = RequestFactory()
        self.request = request_factory.get('/report/mypage/')
        self.request.user = User.objects.get(pk=1)
        self.client.post('/report/report_entries/',
                         {'report_author': self.request.user,
                          'report_title': 'test title',
                          'report_content': 'test'
                          })
        self.client.post('/report/report_entries/',
                         {'report_author': self.request.user,
                          'report_title': 'search test',
                          'report_content': 'search'
                          })

        self.client.post('/report/report_entries/',
                         {'report_author': self.request.user,
                          'report_title': 'search ',
                          'report_content': 'This is search '
                          })

    """
        status_code = 302: created new score.
        status_code = 200: not create new score.
    """

    def test_search(self):
        query_search_word = 'search'
        search_words = query_search_word.split()
        search_reports = []
        for i in range(len(search_words)):
            search_reports += Report.objects.filter(Q(report_content__contains=search_words[i]))
        count = len(search_reports)
        self.assertEqual(count, 2)
