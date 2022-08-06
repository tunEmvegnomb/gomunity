from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User as UserModel


class SignUpTest(APITestCase):
    def test_signup(self):
        url = reverse("signup")
        user_data = {
            "username" : "testuser",
            "nickname" : "testname",
            "email" : "test@gmail.com",
            "password" : "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 200)

class LoginUserTest(APITestCase):
    def setUp(self):
        
        self.data = {'username':'youngsang', 'password': '1234'}
        self.user = UserModel.objects.create_user('youngsang', '1234')
    
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code,200)