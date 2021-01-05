from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from .models import Company, CompanyUser, ROLES, COMPANY_ADMIN
from user.models import CustomUser

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'logo',)


class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = '__all__'


class CreateEmployeeSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField() # company_id does not exist on the CustomUser model. this should not work

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'company_id')
