from rest_framework import permissions
from rest_framework import generics
from .models import COMPANY_ADMIN
from .serializers import CompanySerializer, CompanyUserSerializer

class CreateCompanyView(generics.CreateAPIView):
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        company = serializer.save()
        payload = {'company': company, 'user': self.request.user, 'role': COMPANY_ADMIN}
        company_user = CompanyUserSerializer(data=payload)
        if company_user.is_valid():
            company_user.save()
            return company.data
        return serializer.errors
