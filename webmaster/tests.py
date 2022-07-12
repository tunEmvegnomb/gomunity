from django.test import TestCase
from .models import Notice as NoticeModel
from user.models import User as UserModel
from rest_framework.test import APITestCase
from django.urls import reverse


# Create your tests here.
class NoticeListTest(APITestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user('admin', '123')
        title = "거뮤니티 ver.1.0 개발노트"
        content = "회원가입, 로그인, 공지사항, 질문 답글 게시판이 추가되었습니다"

        self.data = {
            "user" : self.user,
            "title" : title,
            "content": content
        }

        self.notice = NoticeModel.objects.create(**self.data)
        self.user = NoticeModel.objects.all()
        print(self.user)

    
    def test_notice(self):
        # url = reverse('list_notice')
        # print(url)
        response = self.client.get(reverse('webmaster:list_notice'), self.data)
        self.assertEqual(response.status_code,200)