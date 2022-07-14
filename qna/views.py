from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (QnAQuestion as QnAQuestionModel)
from .serializers import QuestionSerializer


# Create your views here.
class QuestionView(APIView):
    # 질문글 조회하기 API
    def get(self, request):
        questions = QnAQuestionModel.objects.all()
        return Response(QuestionSerializer(questions, many=True).data)
    
    # 질문글 작성하기 API
    def post(self, request):
        # request.data['user'] = request.user.id 
        question_serializer = QuestionSerializer(data=request.data)
        if question_serializer.is_valid():
            question_serializer.save(user=self.request.user)
            return Response({"message":"질문글 작성에 성공했다북!"})
        else:
            print(f"에러메시지{question_serializer.errors}")
            return Response({"message":"질문글 작성에 실패했다북..."})
        
    #질문글 수정하기 API
    def put(self, request):
        question = QnAQuestionModel.objects.get(id=id)
        question_serializer = QuestionSerializer(question, data=request.data, partial=True)
        if question_serializer.is_vaild():
            question_serializer.save(user=self.request.user)
            return Response({"message":"수정에 성공했다북!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"수정할 내용을 전부 입력해라북!"}, status=status.HTTP_400_BAD_REQUEST)

    #질문글 삭제하기 API
    def delete(self, request, id):
        question = QnAQuestionModel.objects.get(id=id)
        question.delete()
        return Response({"message":"질문 게시글이 삭제되었다북!"}, status=status.HTTP_200_OK)