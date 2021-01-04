import shutil
import tempfile
from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from user.tests import create_user
from django.test import TestCase
from test_utils.files import get_image_for_upload

MEDIA_ROOT = tempfile.mkdtemp()
CREATE_COMPANY_URL = reverse('company:create')

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
        payload = {
            'name': 'White Canvas',
            'logo': get_image_for_upload()
        }
        res = self.client.post(CREATE_COMPANY_URL, payload, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class PrivateCompanyAPITests(TestCase):
    def setUp(self):
        self.user = create_user(
            email='email@test.com',
            password='testpass',
            name='name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)  # delete the temp dir
        super().tearDownClass()

    def test_create_company_successful(self):
        payload = {
            'name': 'White Canvas',
            'logo': get_image_for_upload()
        }
        res = self.client.post(CREATE_COMPANY_URL, payload, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
