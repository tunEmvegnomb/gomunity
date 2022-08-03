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
            password = request.data['password']
            password2 = request.data['password2']
            if password != password2:
                return Response({"message":"패스워드를 동일하게 해주라북."}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"message":"회원가입 성공이다북"}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request):
        return
    
    def delete(self, request):
        return