from rest_framework import serializers
from user.models import User as UserModel

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user
    
    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    # 포스트맨 작성시 저장되지 않게 하여 계속 찍어볼 수 있음
    # def create(self, validate_data):
    #     return UserModel(**validaate_data)

    def validate(self, data):
        if UserModel.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError(
                detail={"error": "중복된 아이디가 존재합니다"},)

        if UserModel.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError(
                detail={"error": "중복된 이메일이 존재합니다"},)

        condition = all(x not in ["!", "@", "#", "$", "%", "^", "&", "*", "_"] for x in data["password"])
        if len(data["username"]) < 4:
            raise serializers.ValidationError(
                detail={"error": "아이디는 4자 이상 입력해주세요."},)
        elif len(data["password"]) < 8 or condition:
            raise serializers.ValidationError(
                detail={"error": "비밀번호는 8자 이상 특수문자 포함해 입력해주세요"},)
        return data
        
