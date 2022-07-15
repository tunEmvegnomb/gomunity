from django.db import models
from user.models import User as UserModel

# Create your models here.
class QnAQuestion(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="질문작성자", on_delete=models.SET_NULL, null=True)
    title = models.CharField("제목", max_length=100)
    content = models.TextField("질문글")
    like = models.ManyToManyField('user.User', related_name="question_like", through="QuestionLike")
    created_at = models.DateTimeField("생성시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정시간", auto_now=True)

    def __str__(self):
        return f"작성된 질문은 {self.title} 입니다"
        
class QnAAnswer(models.Model):
	user = models.ForeignKey(UserModel, verbose_name="답변자", on_delete=models.SET_NULL, null=True)
	question = models.ForeignKey(QnAQuestion, verbose_name="질문", on_delete=models.SET_NULL, null=True)
	content = models.TextField("답변")
	like = models.ManyToManyField('user.User', related_name="answer_like", through="AnswerLike")
	is_selected = models.BooleanField("채택여부")

	def __str__(self):
		return f"작성된 글 {self.question.title} 의 {self.user.nickname} 의 답변"

class QuestionLike(models.Model):
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	question = models.ForeignKey(QnAQuestion, on_delete=models.CASCADE)

class AnswerLike(models.Model):
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
	answer = models.ForeignKey(QnAAnswer, on_delete=models.CASCADE)