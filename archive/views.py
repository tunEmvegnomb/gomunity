from webbrowser import get
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Archive as ArchiveModel,
    ArchiveAnswer as ArchiveAnswerModel,
    ArchiveLike as ArchiveLikeModel,
    ArchiveAnswerLike as ArchiveAnswerLikeModel,
    )
from .serializers import ArchiveAnswerSerializer, ArchiveSerializer


# Create your views here.

class ArchiveView(APIView):
    
    # 자료게시판 상세 조회 API
    def get(self, request, archive_id):
        archive_articles = ArchiveModel.objects.get(id=archive_id)
        return Response(ArchiveSerializer(archive_articles).data, status=status.HTTP_200_OK)
    
    # 자료 게시글 작성 API
    def post(self, request):
        archive_serializer = ArchiveSerializer(data=request.data)
        if archive_serializer.is_valid():
            archive_serializer.save(user=self.request.user)
            return Response ({"message" : "자료글 작성됐다북"}, status=status.HTTP_200_OK)
            # return Response(archive_serializer.data, status=status.HTTP_200_OK)
        return Response(archive_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 자료 게시글 수정 API
    def put(self, request, archive_id):
        archive = ArchiveModel.objects.get(id=archive_id)
        archive_serializer = ArchiveSerializer(archive, data=request.data, partial=True)
        if archive_serializer.is_valid():
            archive_serializer.save()
            # return Response(archive_serializer.data, status=status.HTTP_200_OK)
            return Response({"message":"수정이 완료되었다북"})
        return Response(archive_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 자료 게시글 삭제 API
    def delete(self, request, archive_id):
        archive = ArchiveModel.objects.get(id=archive_id)
        archive.delete()
        return Response({"message":"자료 게시글이 삭제되었다북!"}, status=status.HTTP_200_OK)
    
    
class ArchiveAnswerView(APIView):
    
    # 자료게시글 답변 작성 API
    def post(self, request, archive_id):
        target_archive = ArchiveModel.objects.get(id=archive_id)
        answer_serializer = ArchiveAnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            after_valid_datas = {
                "user":request.user,
                "archive":target_archive,
            }
            answer_serializer.save(**after_valid_datas)
            return Response({"message": "답변 작성 고맙거북"}, status=status.HTTP_200_OK)
        return Response(answer_serializer.errors)
    
    # 자료게시글 답변 수정 API    
    def put(self, request, answer_id):
        answer = ArchiveAnswerModel.objects.get(id=answer_id)
        answer_serializer = ArchiveAnswerSerializer(answer, data=request.data, partial=True)
        if answer_serializer.is_valid():
            answer_serializer.save(user=self.request.user)
            return Response({"message": "답변 수정 고맙거북"}, status=status.HTTP_200_OK)
        return Response(answer_serializer.errors)
    
    # 자료게시글 답변 삭제 API
    def delete(self, request, answer_id):
        answer = ArchiveAnswerModel.objects.get(id=answer_id)
        answer.delete()
        return Response({"message":"소중한 답변이 삭제됐다북"})
    
    
class LikeArchiveView(APIView):
    def post(self, request, archive_id):
        # return Response({"message":"좋아요 테스트"})
        user = request.user
        target_archive_like = ArchiveLikeModel.objects.filter(archive=archive_id, user=user)
        if not target_archive_like:
            target_archive = ArchiveModel.objects.get(id=archive_id)
            target_archive_like = ArchiveLikeModel.objects.create(archive=target_archive, user=user)
            return Response({"message":"좋아요를 눌렀다북!"},status=status.HTTP_200_OK)
        target_archive_like.delete()
        return Response({"message":"좋아요를 취소했다북.."},status=status.HTTP_200_OK)


class LikeArchiveAnswerView(APIView):
    def post(self, request, answer_id):
        user = request.user
        target_answer_like = ArchiveAnswerLikeModel.objects.filter(archive_answer=answer_id, user=user)
        if not target_answer_like:
            target_answer = ArchiveAnswerModel.objects.get(id=answer_id)
            target_answer_like = ArchiveAnswerLikeModel.objects.create(archive_answer=target_answer, user=user)
            return Response({"message":"좋아요를 눌렀다북!"},status=status.HTTP_200_OK)
        target_answer_like.delete()
        return Response({"message":"좋아요를 취소했다북.."},status=status.HTTP_200_OK)
            
    

class ArchivelistView(APIView):
    def get(self, request):
        archives_list = ArchiveModel.objects.all().order_by('-created_at')
        return Response(ArchiveSerializer(archives_list, many=True).data)
        
