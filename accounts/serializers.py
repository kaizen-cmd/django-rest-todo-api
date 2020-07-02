from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    def save(self):
        user = User(email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'email already used'})
        if password != password2:
            raise serializers.ValidationError({'error': 'password not matching'})
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        return token.key

           