from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from user.tests import create_user
from django.test import TestCase


CREATE_COMPANY_URL = reverse('company:create')


class PublicCompanyAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_company_fails(self):
        payload = {
            'name': 'White Canvas'
        }
        res = self.client.post(CREATE_COMPANY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

class PrivateCompanyAPITests(TestCase):
    def setUp(self):
        self.user = create_user(
            email='email@test.com',
            password='testpass',
            name='name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def test_create_company_successful(self):
        payload = {
            'name': 'White Canvas',
            'image': self.get_image_file() # TODO
        }
        res = self.client.post(CREATE_COMPANY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
