from django.shortcuts import render
from rest_framework.views import APIView
from .models import Notice as NoticeModel
from .serializers import NoticeSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class NoticeView(APIView):
    def get(self, request):
        notices = NoticeModel.objects.all()
        notices_serializer = NoticeSerializer(notices, many=True).data
        return Response(notices_serializer)
    
    def post(self, request):
        # request.data['user'] = request.user.id
        notice_serializer = NoticeSerializer(data=request.data)
        if notice_serializer.is_valid():
            notice_serializer.save(user=self.request.user)
            return Response({"message" : "공지사항 작성에 성공했다북!"}, status=status.HTTP_200_OK)
        else:
            print(notice_serializer.errors)
            return Response({"message" : "공지사항 작성에 실패했다북..."}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        notice = NoticeModel.objects.get(id=id)
        notice_serializer = NoticeSerializer(notice, data=request.data, partial=True)

        if notice_serializer.is_valid():
            notice_serializer.save(user=self.request.user)
            return Response({"message":"수정에 성공했다북"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"수정에 실패했다북"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        notice = NoticeModel.objects.get(id=id)
        notice.delete()
        return Response({"message":"공지 게시글이 삭제되었다북!"}, status=status.HTTP_200_OK)
