from ast import Delete
from pdb import post_mortem
from django import views
from django.urls import path
from . import views
# from .views import QuestionSearchView

# question_search = QuestionSearchView.as_view({
#     'get': 'list'
# })

urlpatterns = [
    path('', views.QuestionView.as_view(), name='question'),
    path('<int:question_id>/', views.QuestionView.as_view(), name='detail_question'),
    path('list/search/', views.QuestionSearchView.as_view(), name='question_search'),
    path('<question_id>/answer/', views.AnswerView.as_view(), name='post_answer'),
    path('answer/<answer_id>/', views.AnswerView.as_view(), name='qna_answer'),
    path('list/', views.QuestionlistView.as_view(), name='list_view'),
    path('like/question/<question_id>/', views.LikeQuestionView.as_view(), name='like_question'),
    path('like/answer/<answer_id>/', views.LikeAnswerView.as_view(), name='like_answer'),
    path('recommend/<question_id>/', views.QuestionRecommendView.as_view(), name='qna_recommend'),
    path('upload/', views.ImageUploadView.as_view(), name='hook_upload'),
]


