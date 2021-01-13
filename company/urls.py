from django.urls import path
from rest_framework.routers import Route
from . import views

app_name = 'company'

urlpatterns = [
    path('<int:pk>/', views.RetrieveCompanyView.as_view(), name='get'),
    path('user/<int:user_id>/', views.RetrieveCompaniesForUserListView.as_view(), name='user-companies'),
    path('create/', views.CreateCompanyView.as_view(), name='create'),
    path('employee/add', views.CreateEmployeeView.as_view(), name='employee-add'),
]
