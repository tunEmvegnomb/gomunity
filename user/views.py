from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from user.serializers import UserSignUpSerializer
from user.jwt_claim_serializer import GomunityTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class GomunityTokenObtainPairView(TokenObtainPairView):
    serializer_class = GomunityTokenObtainPairSerializer

class UserView(APIView):
    def get(self, request):
        return
    
    # 회원가입
    def post(self, request):
        print(request.data)
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()        
            return Response({"message":"회원가입 성공이다북"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        return
    
    def delete(self, request):
        return