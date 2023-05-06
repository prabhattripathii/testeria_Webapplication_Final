import json

from django.shortcuts import render

from testseries_app.models import *


# Create your views here.
def studentDashboardFun(request):
    paper_obj = TestPaper.objects.filter(test_category=2)
    return render(request, 'student_dashboard/student_dashboard_index.html',{'paper':paper_obj})


def studentTestFun(request,id):
    questions = Question.objects.filter(test_paper=id)
    data = []
    for num, q in enumerate(questions, start=1):
        options = Option.objects.filter(question=q)
        options_text = [o.text for o in options]
        question_data = {
            'numb': num,
            'question': q.text,
            'answer': options.filter(is_correct=True).first().text,
            'options': options_text
        }
        data.append(question_data)
        print(data)
    return render(request, 'live_test/index.html', {"data": data})


# def studentTestFun(request,id):
#     test_paper = TestPaper.objects.get(id=1)
#     question = test_paper.get_question_by_index(2)

    print("qqqqq",question)
    return render(request, 'live_test/index.html', {"data": question})



def studentExamPagetFun(request):
    return render(request, 'student_dashboard/student_exams.html')


def studentTestSeriesFun(request):
    return render(request, 'student_dashboard/student_test_series.html')


def studentStudyMaterialFun(request):
    return render(request, 'student_dashboard/student_study_material.html')
