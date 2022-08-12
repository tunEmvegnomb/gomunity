from django.db import models
from user.models import User as UserModel

# Create your models here.
class Archive(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="자료게시판 작성자", on_delete=models.CASCADE)
    category = models.ForeignKey("archive.ArchiveCategory", verbose_name="자료게시판 카테고리", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=100)
    content = models.TextField("본문")
    image = models.ImageField("썸네일 이미지", upload_to='')
    like = models.ManyToManyField(UserModel, related_name='archive_like', through='ArchiveLike')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtag = models.TextField("해시태그", null=True)


class ArchiveAnswer(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="답변자", on_delete=models.CASCADE)
    archive = models.ForeignKey("archive.Archive", verbose_name="자료", on_delete=models.CASCADE)
    content = models.TextField("답변")
    like = models.ManyToManyField(UserModel, related_name='archive_answerlike', through='ArchiveAnswerLike')
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ArchiveCategory(models.Model):
    category = models.CharField("카테고리", max_length=50)
    
    def __str__(self):
        return f"{self.category} 게시판"



class ArchiveLike(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    archive = models.ForeignKey("archive.Archive", on_delete=models.CASCADE)


class ArchiveAnswerLike(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    archive_answer = models.ForeignKey("archive.ArchiveAnswer", on_delete=models.CASCADE)