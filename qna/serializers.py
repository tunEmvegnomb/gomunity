from rest_framework import serializers
from .models import QnAQuestion as QnAQuestionModel, QnAAnswer as QnAAnswerModel

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = QnAAnswerModel
		fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, source="qnaanswer_set", read_only=True)
    class Meta:
        model = QnAQuestionModel
        fields = "__all__"
        