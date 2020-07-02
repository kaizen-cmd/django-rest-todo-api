from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.

class UserRegisterView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user_serializer = serializers.UserRegisterSerializer(data=request.data)
        if user_serializer.is_valid():
            key = user_serializer.save()
            return Response({"username": user_serializer.data['username'], "token": key})
        return Response(user_serializer.errors)
