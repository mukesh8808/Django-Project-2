from django.urls import path
from . import views

urlpatterns = [
    path('', views.Super_Admin_Panel.as_view()),
    path('companies/', views.company_List, name='companies'),
    path('register-company/', views.Register_Company.as_view()),
    path('modules/<id>/', views.module_List, name='modules'),
    path('register-module/', views.Register_Module.as_view()),
]