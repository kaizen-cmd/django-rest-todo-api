from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.UserRegisterView.as_view()),
    path('login/', obtain_auth_token),
]