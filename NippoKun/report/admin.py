from django.contrib import admin

from .models import Report, Score

# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_author', 'report_title', 'report_content', 'created_at', 'updated_at',)


admin.site.register(Report, ReportAdmin)


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'score_author', 'score', 'evaluate_point', 'comment', 'total_score')


admin.site.register(Score, ScoreAdmin)
