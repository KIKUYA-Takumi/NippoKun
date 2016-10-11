from django import forms

from .models import Report, Score


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('report_title', 'report_content')


class SearchForm(forms.Form):
    search_word = forms.CharField(min_length=1, max_length=30)


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('score', 'evaluate_point', 'comment',)
