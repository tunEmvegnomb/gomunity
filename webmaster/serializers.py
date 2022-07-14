from rest_framework import serializers
from .models import Notice as NoticeModel

class NoticeListSerializer(serializers.ModelSerializer):
	class Meta:
		model = NoticeModel
		fields = ["title"]


class NoticeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NoticeModel
        fields = "__all__"
        
