import logging
from rest_framework import serializers
from user.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from .models import Company, CompanyUser, ROLES, COMPANY_ADMIN

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'logo',)


class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = '__all__'


class CompanyUserCreateSerializer(serializers.Serializer):
    company = CompanySerializer()

