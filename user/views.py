from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSignUpSerializer


# Create your views here.
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
        else:
            print(serializer.errors)
            return Response({"message":"실패했다 넌 실패했따 패배했다"}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        return
    
    def delete(self, request):
        return