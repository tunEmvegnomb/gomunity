from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User as UserModel

# Create your tests here.
class LoginUserTest(APITestCase):
    def setUp(self):
        
        self.data = {'username':'youngsang', 'password': '1234'}
        self.user = UserModel.objects.create_user('youngsang', '1234')
    
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code,200)