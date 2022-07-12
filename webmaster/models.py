from django.db import models
from user.models import User as UserModel

# Create your models here.

class Notice(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    title = models.TextField("제목", max_length = 100)
    content = models.TextField("본문")
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)

    def __str__(self):
        return self.title