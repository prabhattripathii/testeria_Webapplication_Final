from django.shortcuts import render
from .models import *
# Create your views here.


def get_test_papers(request,name):
    obj_test_papers = TestPaper.objects.all()
    # print("aaaa",obj_test_serires.get_test_paper_count())


