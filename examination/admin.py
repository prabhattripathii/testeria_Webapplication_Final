# from django.contrib import admin
# from .models import Exam, ExamCategory, Option, Question, Subject, TestPaper, Exam_Description, TestSeries
#
#
# class ExamInline(admin.TabularInline):
#     model = Exam
#     extra = 0
#
#
# class ExamCategoryInline(admin.TabularInline):
#     model = ExamCategory
#     extra = 0
#
#
# class OptionInline(admin.TabularInline):
#     model = Option
#     extra = 0
#
# class TestPaperInline(admin.TabularInline):
#     model = TestPaper
#     # inlines = [QuestionInline]
#     extra = 3
#
#
# class QuestionInline(admin.TabularInline):
#     model = Question
#     extra = 5
#     # inlines = [OptionInline]
#
# class SubjectInline(admin.TabularInline):
#     model = Subject
#     inlines = [QuestionInline]
#
#
# # class TestSeriesInline(admin.TabularInline):
# #     model = TestSeries
# #     inlines = [QuestionInline]
#
#
# @admin.register(ExamCategory)
# class ExamCategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     inlines = [ExamInline]
#     search_fields = ['name']
#
#
# @admin.register(Exam)
# class ExamAdmin(admin.ModelAdmin):
#     list_display = ['name', 'total_marks', 'duration', 'categories']
#     inlines = [SubjectInline]
#     search_fields =  ['name']
#
# @admin.register(TestPaper)
# class TestPaperAdmin(admin.ModelAdmin):
#     list_display = ['test_series_name',]
#     inlines = [QuestionInline]
#     search_fields =  ['test_series_name']
#
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [OptionInline]
#
#
# admin.site.register(Subject)
# admin.site.register(Exam_Description)
# admin.site.register(TestSeries)
