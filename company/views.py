from rest_framework import permissions
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

    def perform_create(self, serializer):
        user = serializer.save()
        CompanyUser.objects.create(user=user, company=serializer.company_id)
        return user


class AddCompanyEmployeeView(generics.CreateAPIView):
    serializer_class = CompanyUserSerializer
    permission_classes = []
