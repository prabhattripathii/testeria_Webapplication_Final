from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogPageFun),
    path('details/<int:id>/', views.blog_description,name="blog_details")
]
