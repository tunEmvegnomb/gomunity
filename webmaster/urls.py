from django.urls import path
from . import views

urlpatterns = [
    path('list_notice', views.NoticeListView.as_view(), name='list_notice'),
]