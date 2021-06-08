
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    re_path(r'register/', views.RegisterApiView.as_view()),
    re_path(r'login/', views.LoginApiView.as_view()),
    re_path(r'user/', views.UserAPIView.as_view()),
]