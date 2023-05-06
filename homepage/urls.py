from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepageFunction),
    path('products', views.productPageFunction),
    path('exam/details/<int:id>', views.examDetailsFunction, name="details")
]