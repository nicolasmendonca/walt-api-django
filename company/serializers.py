from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from .models import Company
from .relationships import CompanyUser, ROLES, COMPANY_ADMIN
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
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True)

    def create(self, validated_data):
        company = validated_data.pop('company_id')
        custom_user = super().create(validated_data)
        CompanyUser.objects.create(
            user=custom_user,
            company=company,
        )
        return custom_user

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'company_id')
