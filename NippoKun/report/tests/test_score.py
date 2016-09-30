from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User

from ..models import Score, Report
# Create your tests here.


class CreateScoreTest(TestCase):
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
        self.request.report = Report.objects.get(pk=1)

    """
        status_code = 302: created new score.
        status_code = 200: not create new score.
    """

    def test_create_score_0(self):
        self.client.post('/report/1/score/',
                         {'report': self.request.report,
                          'score_author': self.request.user,
                          'score': 0,
                          'evaluate_point': 'good job',
                          'comment': 'comment'})
        count = Score.objects.count()
        self.assertEqual(count, 0)

    def test_create_score_1(self):
        self.client.post('/report/1/score/',
                         {'report': self.request.report,
                          'score_author': self.request.user,
                          'score': 1,
                          'evaluate_point': 'good job',
                          'comment': 'comment'})
        count = Score.objects.count()
        self.assertEqual(count, 1)

    def test_create_score_5(self):
        self.client.post('/report/1/score/',
                         {'report': self.request.report,
                          'score_author': self.request.user,
                          'score': 5,
                          'evaluate_point': 'good job',
                          'comment': 'comment'})
        count = Score.objects.count()
        self.assertEqual(count, 1)

    def test_create_score_6(self):
        self.client.post('/report/1/score/',
                         {'report': self.request.report,
                          'score_author': self.request.user,
                          'score': 6,
                          'evaluate_point': 'good job',
                          'comment': 'comment'})
        count = Score.objects.count()
        self.assertEqual(count, 0)


class DeleteScoreTest(TestCase):
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
        self.request.report = Report.objects.get(pk=1)

    def test_delete_score(self):
        self.client.post('/report/1/score/',
                                    {'report': self.request.report,
                                     'score_author': self.request.user,
                                     'score': 4,
                                     'evaluate_point': 'good job',
                                     'comment': 'comment'})
        self.request.score = Score.objects.get(pk=1)
        before_count = Score.objects.count()
        self.client.delete('/report/1/delete/1/')
        after_count = Score.objects.count()
        self.assertEqual(before_count, after_count+1)


class UpdateScoreTest(TestCase):
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
        self.request.report = Report.objects.get(pk=1)

    def test_score_update_score(self):
        self.client.post('/report/1/score/',
                                    {'report': self.request.report,
                                     'score_author': self.request.user,
                                     'score': 4,
                                     'evaluate_point': 'good job',
                                     'comment': 'comment'})
        self.request.score = Score.objects.get(pk=1)
        self.client.post('/report/1/edition/1/',
                         {'report': self.request.report,
                          'score_author': self.request.user,
                          'score': 2,
                          'evaluate_point': self.request.score.evaluate_point,
                          'comment': self.request.score.comment})
        self.request.score = Score.objects.get(pk=1)
        self.assertEqual(self.request.score.score, 2)

    def test_score_update_evaluate_point(self):
        self.client.post('/report/1/score/',
                                    {'report': self.request.report,
                                     'score_author': self.request.user,
                                     'score': 4,
                                     'evaluate_point': 'good job',
                                     'comment': 'comment'})
        self.request.score = Score.objects.get(pk=1)
        self.client.post('/report/1/edition/1/',
                         {'report': self.request.report,
                          'score_author': self.request.user,
                          'score': self.request.score.score,
                          'evaluate_point': 'nice',
                          'comment': self.request.score.comment})
        self.request.score = Score.objects.get(pk=1)
        self.assertEqual(self.request.score.evaluate_point, 'nice')

    report = {
        'report_author': self.request.report.report_author,
        'report_title': self.request.report.report_title,
        'report_content': 'update content'
    }
    self.client.post('/report/1/edition/', report)
    self.request.report = Report.objects.get(pk=1)
    self.assertEqual(self.request.report.report_content, 'update content')






