from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *


class UserViewSet(viewsets.GenericViewSet):


    def get_serializer_class(self):
        if self.action == 'register':
            return UserRegisterSerializer
        elif self.action == 'login':
            return UserLoginSerializer
        elif self.action == 'profile':
            return UserProfileSerializer
        

    def get_permissions(self):
        if self.action == 'register':
            return [AllowAny()]
        elif self.action == 'login':
            return [AllowAny()]
        elif self.action == 'profile':
            return [IsAuthenticated()]
        
    @action(detail=False, methods=['post'], url_path='register')
    def register(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token=get_tokens_for_user(user)

        return Response({
            'token': token,
            'message': 'Registration Successful',
            'user': {
                'email': user.email,
                'name': user.name
            }
        }, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
       
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        token = get_tokens_for_user(user)
        
        return Response({
            'token': token,
            'message': 'Login Successful',
            'user': {
                'email': user.email,
                'name': user.name
            }
        }, status=status.HTTP_200_OK)
    

    @action(detail=False, methods=['get'], url_path='profile')
    def profile(self, request):
        
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)