
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginSignupPageFun),
    path('plugin', views.loginProcessFun)
]
