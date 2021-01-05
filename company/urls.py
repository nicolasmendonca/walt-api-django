from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('create/', views.CreateCompanyView.as_view(), name='create'),
    path('employee/add', views.CreateEmployee.as_view(), name='employee-add'),
]
