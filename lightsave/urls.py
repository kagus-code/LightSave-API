
from django.urls import path,re_path,include
from . import views

urlpatterns = [

  # authentication urls
    re_path(r'register/', views.RegisterApiView.as_view()),
    re_path(r'login/', views.LoginApiView.as_view()),
    re_path(r'user/', views.UserAPIView.as_view()),
    re_path(r'logout/', views.LogoutAPIView.as_view()),

    # appliance urls 
    re_path(r'appliances/', views.ApplianceApiView.as_view()),
    re_path(r'appliances-search/', views.SearchAppliance.as_view()),
    re_path(r'custom-app/', views.CustomApplianceView.as_view()),
]