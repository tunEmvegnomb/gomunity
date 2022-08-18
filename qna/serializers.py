from rest_framework import serializers
from .models import QnAQuestion as QnAQuestionModel, QnAAnswer as QnAAnswerModel
# from user.models import User as UserModel


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.nickname
    
    def get_question(self, obj):
        return obj.question.id
    
    class Meta:
        model = QnAAnswerModel
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, source="qnaanswer_set", read_only=True)
    user = serializers.SerializerMethodField()
    image_path = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.nickname

    def get_image_path(self, obj):
        return "/media/" + str(obj.image)

    class Meta:
        model = QnAQuestionModel
        fields = "__all__"
        