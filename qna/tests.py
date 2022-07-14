from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from user.models import User as UserModel
from .models import QnAQuestion as QnAQuestionModel


class QuestionTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username' : 'heejeong', 'password': '1234'}
        cls.question_data = {'title' : '질문이 있습니다!' , 'content' : '도대체 이건 왜 되는거져?'}
        cls.user = UserModel.objects.create_user('heejeong', '1234')
        cls.question = QnAQuestionModel.objects.create(**cls.question_data)

    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']

    def test_post_question(self):
        response = self.client.post(
            path = reverse("question"), 
            data = self.question_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
            )
        self.assertEqual(response.status_code, 200)

    