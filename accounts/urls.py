from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('signup/', views.signup_view, name="signup")

]
