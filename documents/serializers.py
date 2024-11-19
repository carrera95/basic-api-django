from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'id',
            'description',
            'file',
            'type',
            'title',
            'uploaded_at', 
            'created_by', 
            'created_at', 
            'updated_by'
        ]
        read_only_fields = [
            'uploaded_by', 
            'uploaded_at', 
            'created_by', 
            'created_at', 
            'updated_by', 
            'updated_at'
        ]