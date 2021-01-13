from django.urls import path
from rest_framework.routers import Route
from . import views

app_name = 'company'

urlpatterns = [
    path('<int:user_id>/', views.RetrieveCompaniesForUserList.as_view(), name='companies'),
    path('create/', views.CreateCompanyView.as_view(), name='create'),
    path('employee/add', views.CreateEmployee.as_view(), name='employee-add'),
]
