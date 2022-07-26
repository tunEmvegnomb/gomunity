from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.QnAQuestion)
admin.site.register(models.QnAAnswer)
admin.site.register(models.QuestionLike)
admin.site.register(models.AnswerLike)