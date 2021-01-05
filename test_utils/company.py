from company.models import Company
from company.relationships import CompanyUser, COMPANY_ADMIN
from .files import get_image_for_upload

def create_company(name='White Canvas', logo=None, admin=None):
    company_user = None
    if logo is None:
        logo = get_image_for_upload()
    company = Company.objects.create(name=name, logo=logo)
    if admin is not None:
        company_user = CompanyUser.objects.create(user=admin, company=company, role=COMPANY_ADMIN)
    return (admin, company, company_user)
