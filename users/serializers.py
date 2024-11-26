from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True) 
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data): 
        user = User.objects.create_user( 
            username=validated_data['username'], 
            email=validated_data['email'], 
            password=validated_data['password'] 
        )
        
        return user