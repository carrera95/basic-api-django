from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from users.models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({
            'Error': 'Invalid password'
        },  status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({
        'Token': token.key,
        'User': serializer.data
    },  status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)

        return Response({
            'Token': token.key,
            'User': serializer.data
        },status=status.HTTP_200_OK)
    
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )