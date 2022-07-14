from rest_framework import serializers
from .models import QnAQuestion as QnAQuestionModel

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnAQuestionModel
        fields = "__all__"