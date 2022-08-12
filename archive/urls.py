from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArchiveView.as_view(), name='archive'),
    path('list/', views.ArchivelistView.as_view(), name='archive_list'),
    path('<int:archive_id>/', views.ArchiveView.as_view(), name='archive_detail'),

]
