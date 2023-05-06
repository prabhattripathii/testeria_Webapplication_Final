from django.shortcuts import redirect, render
from . import models

# Create your views here.
def loginSignupPageFun(request):

    return render(request,'loginAndSignup.html')

def loginProcessFun(request):
    redirect('student/dashboard')