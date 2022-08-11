from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoticeView.as_view(), name='notice'),
    path('<int:id>', views.NoticeView.as_view(), name='update_notice'),
    
]
