from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.get_test_papers),
    # path('details/<int:id>/', views.blog_description,name="blog_details")
]
