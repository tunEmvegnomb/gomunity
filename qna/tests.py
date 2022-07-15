from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

from user.models import User as UserModel
from .models import (
    QnAAnswer as QnAAnswerModel, 
    QnAQuestion as QnAQuestionModel
    )


class QuestionTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username' : 'heejeong', 'password': '1234'}
        cls.user = UserModel.objects.create_user('heejeong', '1234')

        # 질문글 셋업
        cls.question_data = {'title' : '질문이 있습니다!' , 'content' : '도대체 이건 왜 되는거져?'}
        cls.question = QnAQuestionModel.objects.create(**cls.question_data)
        
        # 답글 셋업
        cls.answer_data = {'content': '마좌엽', 'is_selected': False}
        cls.answer = QnAAnswerModel.objects.create(**cls.answer_data)

    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']

    # 질문 조회 API
    def test_get_question(self):
        response = self.client.get(reverse("question")+"1")
        self.assertEqual(response.status_code, 200)

    # 질문 작성 API
    def test_post_question(self):
        response = self.client.post(
            path = reverse("question"), 
            data = self.question_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
            )
        self.assertEqual(response.status_code, 200)

    # 질문 수정 API
    def test_put_question(self):
        response = self.client.put(
            path = reverse("question")+"1", 
            data = self.question_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
            )
        self.assertEqual(response.status_code, 200)


    # 질문 삭제 API
    def test_delete_question(self):
        response = self.client.delete(
            path = reverse("question")+"1", 
            data = self.question_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
            )
        self.assertEqual(response.status_code, 200)
        
    # 답글 작성 API
    def test_post_answer(self):
        response = self.client.post(
            path = reverse("question") + "1/answer/",
            data = self.answer_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
            )
        self.assertEqual(response.status_code, 200)
        
    # 답글 수정 API
    def test_put_answer(self):
        response = self.client.put(
            path = reverse("question") + "answer/1",
            data = self.answer_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, 200)
    # 답글 삭제 API
    def test_delete_answer(self):
        response = self.client.delete(
            path = reverse("question") + "answer/1",
            data = self.answer_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, 200)