from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArchiveView.as_view(), name='archive'),
    path('list/', views.ArchivelistView.as_view(), name='archive_list'),
    path('<int:archive_id>/', views.ArchiveView.as_view(), name='archive_detail'),
    path('<int:archive_id>/answer/', views.ArchiveAnswerView.as_view(), name='archive_answer'),
    path('answer/<int:answer_id>/', views.ArchiveAnswerView.as_view()),
    path('like/archive/<int:archive_id>/', views.LikeArchiveView.as_view(), name='like_archive'),
    path('like/answer/<int:answer_id>/', views.LikeArchiveAnswerView.as_view(), name='like_answer'),
    
]
