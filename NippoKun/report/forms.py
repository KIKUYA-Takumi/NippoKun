from django import forms

from .models import Report, Score


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('report_title', 'report_content')
        widgets = {
            'report_title': forms.TextInput(attrs={'size': 40}),
            'report_content': forms.Textarea(attrs={'cols': 50, 'rows': 40})
        }


class SearchForm(forms.Form):
    search_word = forms.CharField(min_length=1, max_length=30)


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('score', 'evaluate_point', 'comment',)
        score = forms.ChoiceField(
            choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)),
        )
        widgets = {
            'evaluate_point': forms.TextInput(attrs={'size': 40}),
            'comment': forms.Textarea(attrs={'cols': 50, 'rows': 40})
        }
