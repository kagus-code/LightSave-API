
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    re_path(r'register/', views.RegisterApiView.as_view()),
]