from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import ReportForm, SearchForm, ScoreForm
from .models import Report, Score


# Create your views here.


class CreateReport(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'report/entry.html'

    def form_valid(self, form):
        form.instance.report_author = self.request.user
        return super(CreateReport, self).form_valid(form)

    def get_success_url(self):
        return reverse('report:index')


class ListReport(ListView):
    model = Report
    template_name = 'report/index.html'
    queryset = Report.objects.order_by('-updated_at')


class ListMyReport(ListView):
    model = Report
    template_name = 'report/myreports.html'

    def get_queryset(self):
        return Report.objects.filter(report_author=self.request.user).order_by('-updated_at')


class DetailReport(DetailView):
    model = Report
    template_name = 'report/detail.html'

    def get_success_url(self):
        return reverse('report:detail_report', args=(self.object.id,))


class UpdateReport(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'report/edit.html'

    def get_success_url(self):
        return reverse('report:mypage')


class DeleteReport(DeleteView):
    model = Report
    template_name = 'report/delete.html'
    success_url = reverse_lazy('report:mypage')


def search(request):
    form = SearchForm(request.GET or None)
    if request.method == 'GET':
        if form.is_valid():
            search_words = form.cleaned_data['search_word'].split()
            search_reports = []
            for i in range(len(search_words)):
                search_reports += Report.objects.filter(Q(report_content__contains=search_words[i]))
            return render_to_response(
                'report/search.html',
                {'form': form, 'reports': search_reports},
                RequestContext(request)
            )

        return render(request, 'report/search.html', {'form': form})


class CreateUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'report/user_register.html'

    def get_success_url(self):
        return reverse('report:login')


class CreateScore(CreateView):
    model = Score
    form_class = ScoreForm
    template_name = 'report/score.html'

    def form_valid(self, form):
        form.instance.report = get_object_or_404(Report, pk=self.args[0])
        form.instance.score_author = self.request.user
        return super(CreateScore, self).form_valid(form)

    def get_success_url(self):
        return reverse('report:index')


class UpdateScore(UpdateView):
    model = Score
    form_class = ScoreForm
    template_name = 'report/score_edit.html'

    def get_success_url(self):
        return reverse('report:index')


class DeleteScore(DeleteView):
    model = Score
    template_name = 'report/delete.html'
    success_url = reverse_lazy('report:index')


class ListScore(ListView):
    model = Score,
    template_name = 'report/score_list.html'

    def get_queryset(self):
        return Score.objects.filter(report=self.kwargs['report']).order_by('-scored_at')
