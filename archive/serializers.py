from curses import meta
from rest_framework import serializers
from .models import (
    Archive as ArchiveModel,
    ArchiveAnswer as ArchiveAnswerModel,
    ArchiveLike as ArchiveLikeModel, 
    ArchiveAnswerLike as ArchiveAnswerLikeModel,
    ArchiveCategory as ArchiveCategoryModel,
)


class ArchiveAnswerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    archive = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.nickname
    
    def get_archive(self, obj):
        return obj.archive.id
    
    class Meta:
        model = ArchiveAnswerModel
        # fields = ["user", "archive", "content", "image", "created_at", "updated_at"]
        fields = '__all__'

class ArchiveSerializer(serializers.ModelSerializer):
    archive_answer = ArchiveAnswerSerializer(many=True, source="archiveanswer_set", read_only=True)
        
    user = serializers.SerializerMethodField()
    article_category = serializers.SerializerMethodField(source="category_set")
    
    def get_user(self, obj):
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
    
    class Meta:
        model = ArchiveModel
        fields = ["user", "title", "content", "image", "category", "article_category",
                "hashtag", "like", "archive_answer", "created_at", "updated_at"]
        
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
        
