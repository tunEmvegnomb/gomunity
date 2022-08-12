from rest_framework import serializers
from .models import (
    Archive as ArchiveModel,
    ArchiveAnswer as ArchiveAnswerModel,
    ArchiveLike as ArchiveLikeModel, 
    ArchiveAnswerLike as ArchiveAnswerLikeModel,
    ArchiveCategory as ArchiveCategoryModel,
)


class ArchiveAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveAnswerModel
        fields = "__all__"



class ArchiveSerializer(serializers.ModelSerializer):
    archive_answer = ArchiveAnswerSerializer(many=True, source="archiveanswer_set", read_only=True)
    
    user_nickname = serializers.SerializerMethodField(read_only=True)
    article_category = serializers.SerializerMethodField(source="category_set")
    
    def get_user_nickname(self, obj):
        return obj.user.nickname
    
    def get_article_category(self, obj):
        return obj.category.category
        
    def validate(self, data):
        hashtag_list = data.get("hashtag")
        hashtag_list = hashtag_list.split(" ")
        for i in hashtag_list:
            if not i[0].startswith("#"):
                raise serializers.ValidationError(
                    detail={"error" : "해시태그는 앞에 #을 붙여야 작성할 수 있습니다"}
                )
        return data

    def create(self, validate_data):
        return ArchiveModel(**validate_data)
    
    class Meta:
        model = ArchiveModel
        fields = ["user", "category", "title", "content", "image", 
                "hashtag", "archive_answer", "user_nickname", "article_category"]
        
        extra_kwargs = {
            
            'title': {
                'error_messages': {
                    'required': '제목을 입력해주세요',
                    },
                    'required': True
                    },
            
            'content':{
                'error_messages':{
                    'required': '콘텐츠를 입력해주세요',
                },
                'required': True
            },
            
            'category':{
                'error_messages':{
                'required': '카테고리를 선택해주세요',
                }
            },
            'required':True
        }
        
