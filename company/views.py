from rest_framework import generics, permissions
from rest_framework.response import Response
from user.models import CustomUser
from .models import Company
from .relationships import COMPANY_ADMIN, CompanyUser
from .serializers import CompanySerializer, CreateEmployeeSerializer

class CreateCompanyView(generics.CreateAPIView):
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        company = serializer.save()
        CompanyUser.objects.create(company=company, user=self.request.user, role=COMPANY_ADMIN)
        return company

class CreateEmployee(generics.CreateAPIView):
    serializer_class = CreateEmployeeSerializer

class RetrieveCompaniesForUserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, user_id):
        user = CustomUser.objects.get(pk=user_id)
        queryset = user.companies.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)
