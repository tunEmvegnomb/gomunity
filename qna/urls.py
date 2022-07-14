from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionView.as_view(), name='question'),
    path('<int:id>', views.QuestionView.as_view(), name='update_question'),
]
