from django.test import TestCase
from .models import Notice as NoticeModel
from user.models import User as UserModel
from rest_framework.test import APITestCase
from django.urls import reverse


class NoticeTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username' : 'heejeong', 'password': '1234'}
        cls.notice_data = {'title' : '안녕' , 'content' : '반갑습니다'}
        cls.user = UserModel.objects.create_user('heejeong', '1234')
        cls.notice = NoticeModel.objects.create(**cls.notice_data)

    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']

    # 공지사항 목록 조회 API 
    def test_list_notice(self):
        response = self.client.get(reverse('list_notice'))
        self.assertEqual(response.status_code,200)
        
    # 공지사항 작성하기 API
    def test_post_notice(self):
        response = self.client.post(
            path = reverse("notice"), 
            data = self.notice_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
            )
        self.assertEqual(response.status_code, 200)

    # 공지사항 내용 조회 API
    def test_detail_notice(self):
        response = self.client.get(reverse('notice')) 
        self.assertEqual(response.status_code,200)

    # 공지사항 내용 수정 API
    def test_update_notice(self):
        url = reverse("notice")+"1"
        response = self.client.put(
            path = url,
            data = self.notice_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
            )
        self.assertEqual(response.status_code, 200)