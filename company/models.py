from django.db import models
from django.utils.translation import ugettext_lazy as _
import company.relationships

# company model
class Company(models.Model):
    users = models.ManyToManyField('user.CustomUser', through='company.CompanyUser')
    name = models.CharField(_('name'), max_length=255)
    logo = models.ImageField(_('logo'), upload_to='uploads/logos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
