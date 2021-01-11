from rest_framework import generics
from .models import COMPANY_ADMIN, CompanyUser
from .serializers import CompanySerializer, CompanyUserSerializer, CreateEmployeeSerializer

class CreateCompanyView(generics.CreateAPIView):
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        company = serializer.save()
        CompanyUser.objects.create(company=company, user=self.request.user, role=COMPANY_ADMIN)
        return company

class CreateEmployee(generics.CreateAPIView):
    serializer_class = CreateEmployeeSerializer
