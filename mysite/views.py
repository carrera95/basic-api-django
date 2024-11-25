from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import UserSerializer
from users.models import CustomUser
from django.shortcuts import get_object_or_404

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request): 
    user = get_object_or_404(
        CustomUser, 
        username=request.data['username']
    )

    if not user.check_password(request.data['password']): 
        return Response({ 
            'Error': 'Invalid password' 
        }, status=status.HTTP_400_BAD_REQUEST)
    
    refresh = RefreshToken.for_user(user) 
    access_token = str(refresh.access_token) 
    refresh_token = str(refresh)
    serializer = UserSerializer(instance=user) 
    
    return Response({ 
        'access': access_token, 
        'refresh': refresh_token, 
        'user': { 
            'id': user.id, 
            'username': user.username,
            'email': user.email, 
            'name': user.first_name, 
            'is_admin': user.is_staff 
        } 
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save() 
        user.uncripted_pswd = request.data['password'] 
        user.set_password(serializer.data['password']) 
        user.save()

        refresh = RefreshToken.for_user(user) 
        access_token = str(refresh.access_token) 
        refresh_token = str(refresh)

        return Response({
            'access': access_token, 
            'refresh': refresh_token, 
            'user': serializer.data
        },status=status.HTTP_200_OK)
    
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )