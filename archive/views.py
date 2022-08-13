from webbrowser import get
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Archive as ArchiveModel,
    )
from .serializers import ArchiveSerializer


# Create your views here.

class ArchiveView(APIView):
    
    # 자료게시판 상세 조회 API
    def get(self, request, archive_id):
        archive_articles = ArchiveModel.objects.get(id=archive_id)
        return Response(ArchiveSerializer(archive_articles).data, status=status.HTTP_200_OK)
    
    # 자료 게시글 작성 API
    def post(self, request):
        request.data['user'] = request.user.id
        archive_serializer = ArchiveSerializer(data=request.data)
        if archive_serializer.is_valid():
            archive_serializer.save(user=self.request.user)
            # return Response ({"message" : "자료글 작성됐다북"}, status=status.HTTP_200_OK)
            return Response(archive_serializer.data)
        return Response(archive_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 자료 게시글 수정 API
    def put(self, request, archive_id):
        archive = ArchiveModel.objects.get(id=archive_id)
        archive_serializer = ArchiveSerializer(archive, data=request.data, partial=True)
        if archive_serializer.is_valid():
            archive_serializer.save(user=self.request.user)
            return Response(archive_serializer.data)
            # return Response({"message":"수정이 완료되었다북"})
        return Response(archive_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 자료 게시글 삭제 API
    def delete(self, request, archive_id):
        archive = ArchiveModel.objects.get(id=archive_id)
        archive.delete()
        return Response({"message":"자료 게시글이 삭제되었다북!"}, status=status.HTTP_200_OK)
    
# 자료 게시글 목록 조회 API
class ArchivelistView(APIView):
    def get(self, request):
        archives_list = ArchiveModel.objects.all().order_by('-created_at')
        return Response(ArchiveSerializer(archives_list).data, many=True)
        
