from django.shortcuts import render
from rest_framework.views import APIView
from .models import Notice as NoticeModel
from .serializers import NoticeListSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class NoticeListView(APIView):
    def get(self, request):
        notices = NoticeModel.objects.get(id=1)
        return Response(NoticeListSerializer(notices).data, status=status.HTTP_200_OK)