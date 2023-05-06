from django.contrib import admin
from django.utils.html import format_html

#
# from django.forms.models import modelformset_factory
# from tornado.web import url
#
from .models import TestSeriesCategory, TestSeries, TestPaper, Question, Option, TestSeriesNew
admin.site.site_header = "Admin Testeria Products Management"
admin.site.site_title="Testeria Management"
#
#
# class TestPaperInline(admin.StackedInline):
#     model = TestPaper
#     extra = 1
#
#

#
#
# class OptionInline(admin.StackedInline):
#     model = Option
#     extra = 1
#
#
# admin.site.register(TestSeriesCategory)
#
#
# @admin.register(TestSeries)
# class TestSeriesAdmin(admin.ModelAdmin):
#     inlines = [TestPaperInline]
#     list_display = ('name', 'test_categories', 'isNewSeries1', 'isPopularSeries1')
#
#
# @admin.register(TestPaper)
# class TestPaperAdmin(admin.ModelAdmin):
#     inlines = [QuestionInline]
#     list_display = (
#         'test_category', 'test_series_name', 'paper_type_test', 'total_marks', 'total_question', 'test_year', 'isFree',
#         'options')
#     list_editable = ('options',)
#
#     def options(self, obj):
#         p = [str(i.Option) for i in Option.objects.filter(question=obj.id)]
#         return p
#
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [OptionInline]
#     list_display = ('text', 'marks', 'is_negative', 'test_paper')
#
#
# class OptionAdmin(admin.ModelAdmin):
#     list_display = ('text', 'is_correct', 'question')


from django import forms
from django.contrib import admin

from .models import TestPaper, Option, TestSeriesNew, TestPaperNew

#
# class TestPaperForm(forms.ModelForm):
#     options = forms.CharField(max_length=255)
#     is_correct = forms.BooleanField()
#
#     class Meta:
#         model = Option
#         fields = '__all__'
#
#     def save(self, commit=True):
#         question = super().save(commit=commit)
#         options = self.cleaned_data['options'].split(',')
#         is_correct = self.cleaned_data['is_correct']
#         for i, option_text in enumerate(options):
#             option_is_correct = is_correct
#             option, created = Option.objects.get_or_create(
#                 question=question,
#                 text=option_text.strip(),
#                 defaults={'is_correct': option_is_correct},
#             )
#             if not created:
#                 option.is_correct = option_is_correct
#                 option.save()
#         return question
#
#
# class QuestionInline(admin.StackedInline):
#     model = Question
#     extra = 1
#     fields = ('text', 'marks', 'is_negative','options','is_correct')
#     form = TestPaperForm
#
#     def options(self, obj):
#         p = [str(i.text) for i in Option.objects.get(question=obj.id)]
#         return p
#
#     def is_correct(self, obj):
#         p = [str(i.is_correct) for i in Option.objects.get(question=obj.id)]
#         return p
#
#
# @admin.register(TestPaper)
# class TestPaperAdmin(admin.ModelAdmin):
#     inlines = [QuestionInline]
#
#     list_display = (
#         'test_category', 'test_series_name', 'paper_type_test', 'total_marks', 'total_question', 'test_year', 'isFree',
#         )
#
# admin.site.register(Option)


from django.urls import reverse
from nested_admin import NestedTabularInline, NestedModelAdmin





class OptionInline(NestedTabularInline):
    model = Option
    extra = 4
    max_num = 4


admin.site.register(TestSeriesCategory)

class QuestionAdmin(NestedTabularInline):
    model = Question
    inlines = [OptionInline]
    max_num = 100


@admin.register(TestPaper)
class TestPaperAdmin(NestedModelAdmin):
    inlines = [QuestionAdmin]
    def has_module_permission(self, request):
        return False
# admin.site.register(TestPaper, TestPaperAdmin)

class TestPaperLink(forms.ModelForm):
    class Meta:
        model = TestPaperNew
        fields = '__all__'
        widgets = {
            'test_series_name': forms.TextInput(attrs={'style': 'width: 300px;height:50px;'}),
        }

class TestPaperNewInline(admin.TabularInline):
    model = TestPaperNew
    extra = 4
    max_num = 4
    fields = (
    'test_series_name', 'paper_type_test', 'total_marks', 'total_question', 'test_year', 'isFree', 'test_link')
    readonly_fields = ('test_link',)
    form = TestPaperLink

    def test_link(self, obj):
        # Check whether the instance has a primary key (i.e., has been saved to the database)
        if obj.pk:
            url = reverse('admin:testseries_app_testpaper_change', args=[obj.pk])
            return format_html(f'<a href="{url}">Create Test Paper</a>')
        else:
            return "No link"


@admin.register(TestSeriesNew)
class TestSeriesNewAdmin(admin.ModelAdmin):
    inlines = [TestPaperNewInline]
    max_num = 20
