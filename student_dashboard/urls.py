from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.studentDashboardFun),
    path('starttest/<int:id>', views.studentTestFun),
    path('exams/', views.studentExamPagetFun),
    path('testseries/',views.studentTestSeriesFun),
    path('studymaterial/',views.studentStudyMaterialFun)

]