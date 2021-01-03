from user.models import CustomUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models import CustomUser

SUPER_ADMIN = 'super_admin'
COMPANY_ADMIN = 'company_admin'
COMPANY_EMPLOYEE = 'company_employee'

ROLES = (
    (SUPER_ADMIN, _('super admin')),
    (COMPANY_ADMIN, _('company admin')),
    (COMPANY_EMPLOYEE, _('company employee'))
)


class Company(models.Model):
    name = models.CharField(_('name'), max_length=255)
    logo = models.ImageField(_('logo'), upload_to='uploads/logos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CompanyUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLES, max_length=255, default=COMPANY_EMPLOYEE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.name + ' - ' + self.user.name
