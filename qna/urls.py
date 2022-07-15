from ast import Delete
from pdb import post_mortem
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionView.as_view(), name='question'),
    path('<question_id>', views.QuestionView.as_view(), name='detail_question'),
    path('<question_id>/answer/', views.AnswerView.as_view(), name='post_answer'),
    path('answer/<answer_id>', views.AnswerView.as_view(), name='qna_answer'),
    path('list/', views.QuestionlistView.as_view(), name='list_view'),
]


