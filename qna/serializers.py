from rest_framework import serializers
from .models import QnAQuestion as QnAQuestionModel, QnAAnswer as QnAAnswerModel
from .upload import upload_s3
# from user.models import User as UserModel

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = QnAAnswerModel
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
  
    answer = AnswerSerializer(many=True, source="qnaanswer_set", read_only=True)
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = QnAQuestionModel
        fields = "__all__"
        