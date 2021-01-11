import shutil
import tempfile
from test_utils.company import create_company
from .models import Company
from .relationships import CompanyUser, COMPANY_ADMIN
from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from test_utils.users import create_user
from django.test import TestCase
from test_utils.files import get_image_for_upload

MEDIA_ROOT = tempfile.mkdtemp()
CREATE_COMPANY_URL = reverse('company:create')
CREATE_EMPLOYEE_URL = reverse('company:employee-add')

def generate_successful_payload():
    return {
        'name': 'White Canvas',
        'logo': get_image_for_upload()
    }

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PublicCompanyAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    @classmethod
    def tearDownClass(cls):
        # not used, since unauthenticated users can't create companies
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)  # delete the temp dir
        super().tearDownClass()

    def test_create_company_fails(self):
        payload = generate_successful_payload()
        res = self.client.post(CREATE_COMPANY_URL, payload, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PrivateCompanyAPITests(TestCase):
    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)  # delete the temp dir
        super().tearDownClass()

    def test_create_company_successful(self):
        payload = generate_successful_payload()
        res = self.client.post(CREATE_COMPANY_URL, payload, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(payload['name'], res.data['name'])

    def test_create_company_is_stored_on_db(self):
        """Test storing company and companyuser data"""
        payload = generate_successful_payload()
        res = self.client.post(CREATE_COMPANY_URL, payload, format='multipart')
        created_company = Company.objects.get(name=res.data['name'])
        self.assertIsInstance(created_company, Company)
        self.assertEqual(created_company.name, payload['name'])

        created_companyuser = CompanyUser.objects.get(company=created_company, user=self.user)
        self.assertIsInstance(created_companyuser, CompanyUser)
        self.assertEqual(created_companyuser.role, COMPANY_ADMIN)

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PrivateCreateEmployeeAPITests(APITestCase):
    def setUp(self):
        (self.user, self.company, self.company_user) = create_company(admin=create_user())
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_employee_success(self):
        payload = {
            'company_id': self.company.id,
            'email': 'employee@test.com',
            'name': 'Employee 1'
        }
        res = self.client.post(CREATE_EMPLOYEE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
