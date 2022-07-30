from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    QnAQuestion as QnAQuestionModel,
    QuestionLike as QuestionLikeModel,
    AnswerLike as AnswerLikeModel
                     )
from .serializers import QuestionSerializer, AnswerSerializer, QnAAnswerModel

from .upload import upload_s3

# Create your views here.
class QuestionView(APIView):
    # 질문글 상세 조회하기 API
    def get(self, request, question_id):
        target_question = QnAQuestionModel.objects.get(id=question_id)
        question_serializer = QuestionSerializer(target_question).data
        return Response(question_serializer)
    
    
    # 질문글 작성하기 API
    def post(self, request):
        question_serializer = QuestionSerializer(data=request.data)
        if question_serializer.is_valid():
            question_serializer.save(user=self.request.user)
            image = f"media/{request.data['image']}"
            upload_url = upload_s3(image)
                


            # question_serializer.save(user=self.request.user)
            return Response({"message":"질문글 작성에 성공했다북!"})
        else:
            print(question_serializer.errors)
            print(f"에러메시지{question_serializer.errors}")
            return Response({"message":"질문글 작성에 실패했다북..."})
        
    #질문글 수정하기 API
    def put(self, request, question_id):
        question = QnAQuestionModel.objects.get(id=question_id)
        question_serializer = QuestionSerializer(question, data=request.data, partial=True)
        if question_serializer.is_valid():
            question_serializer.save(user=self.request.user)
            return Response({"message":"수정에 성공했다북!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"수정할 내용을 전부 입력해라북!"}, status=status.HTTP_400_BAD_REQUEST)

    #질문글 삭제하기 API
    def delete(self, request, question_id):
        question = QnAQuestionModel.objects.get(id=question_id)
        question.delete()
        return Response({"message":"질문 게시글이 삭제되었다북!"}, status=status.HTTP_200_OK)




class AnswerView(APIView):
    def post(self, request, question_id):
        target_question = QnAQuestionModel.objects.get(id=question_id)
        # request.data['is_selected'] = False
        # request.data['user'] = request.user.id
        # request.data['question'] = target_question.id
        answer_serializer = AnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            after_valid_datas = {
                "user": request.user,
                "question":target_question,
                "is_selected": False
            }
            answer_serializer.save(**after_valid_datas)
            return Response({"message": "답변 작성 고맙거북"}, status=status.HTTP_200_OK)
        else:
            print(answer_serializer.errors)
            return Response({"message": "답변 작성 실패거북"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, answer_id):
        answer = QnAAnswerModel.objects.get(id=answer_id)
        answer_serializer = AnswerSerializer(answer, data=request.data, partial=True)

        if answer_serializer.is_valid():
            answer_serializer.save(user=self.request.user)
            return Response({"message":"답변 수정됐다북"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"답변 수정에 실패했다북!"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, answer_id):
        answer = QnAAnswerModel.objects.get(id=answer_id)
        answer.delete()

        return Response({"message":"소중한 답변이 삭제됐다북"})


class QuestionlistView(APIView):
    def get(self, request):
        questions = QnAQuestionModel.objects.all().order_by('-created_at')
        return Response(QuestionSerializer(questions, many=True).data)
    

class LikeQuestionView(APIView):
    def post(self, request, question_id):
        user = request.user
        target_question_like = QuestionLikeModel.objects.filter(question=question_id, user=user)
        if not target_question_like:
            target_question = QnAQuestionModel.objects.get(id=question_id)
            target_question_like = QuestionLikeModel.objects.create(question=target_question, user=user)
            return Response({"message":"좋아요를 눌렀다북!"},status=status.HTTP_200_OK)
        else:
            target_question_like.delete()
            return Response({"message":"좋아요를 취소했다북.."},status=status.HTTP_200_OK)

class LikeAnswerView(APIView):
    def post(self, request, answer_id):
        print("답글 좋아요 API 작동하라!")
        user = request.user
        target_answer_like = AnswerLikeModel.objects.filter(answer=answer_id, user=user)
        if not target_answer_like:
            target_answer = QnAAnswerModel.objects.get(id=answer_id)
            target_answer_like = AnswerLikeModel.objects.create(answer=target_answer, user=user)
            return Response({"message":"좋아요를 눌렀다북!"},status=status.HTTP_200_OK)
        else:
            target_answer_like.delete()
            return Response({"message":"좋아요를 취소했다북.."},status=status.HTTP_200_OK)