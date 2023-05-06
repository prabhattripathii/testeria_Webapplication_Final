from django.shortcuts import render, get_object_or_404

from examination.models import ExamCategory, Exam, Exam_Description

from testseries_app.models import TestSeries


# from testeria_webapplcation.examination.models import Exam_Description


# Create your views here.
# def homepageFunction(request):
#     exam_category = ExamCategory.objects.all()
#
#     return render(request, "index.html", {'examCategory': exam_category})


def homepageFunction(request):
    exam_category = ExamCategory.objects.all()
    exam_name = Exam.objects.all()
    obj_test_serires = TestSeries.objects.all()

    data = {'examCategory': exam_category,
            'exam_name': exam_name,
            'test_series': obj_test_serires
            }

    return render(request, "index.html", context=data, )


def productPageFunction(request):
    return render(request, 'e_comm/e_comm_index.html')


def examDetailsFunction(request, id):
    exam_descp = get_object_or_404(Exam_Description, id=id)

    return render(request, 'main_site/exam_details.html', {"exam_descp": exam_descp.exam_description})
