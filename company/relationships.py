from django.db import models
from django.utils.translation import ugettext_lazy as _


SUPER_ADMIN = 'super_admin'
COMPANY_ADMIN = 'company_admin'
COMPANY_EMPLOYEE = 'company_employee'

ROLES = (
    (SUPER_ADMIN, _('super admin')),
    (COMPANY_ADMIN, _('company admin')),
    (COMPANY_EMPLOYEE, _('company employee'))
)

# relationship model
class CompanyUser(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    role = models.CharField(choices=ROLES, max_length=255, default='company_employee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.name + ' - ' + self.user.name
