from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'id',
            'description',
            'file',
            'file_type'
        ]
        read_only = [
            'uploaded_by',
            'uploaded_at'
        ]