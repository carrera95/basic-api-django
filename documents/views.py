from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.exceptions import NotFound
from .models import Document
from .serializers import DocumentSerializer
from .utils import get_unique_filename

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    # Create (POST)
    def create(self, request): 
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data) 
        
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )
    
    def perform_create(self, serializer):
        file = serializer.validated_data['file'] 
        file.name = get_unique_filename(file.name) 
        file_type = file.content_type

        if file_type.startswith('application/'): 
            file_type = file_type[len('application/'):] 
        elif file_type.startswith('image/'): 
            file_type = file_type[len('image/'):]

        serializer.save(
            created_by=self.request.user,
            title=file.name, 
            type=file_type,
            file=file
        )

    # List (GET)
    def list(self, request):
        documents = self.get_queryset()
        serializer = self.get_serializer(documents, many=True)
        
        return Response(serializer.data)

    # Detail (GET)
    def retrieve(self, request, pk=None):
        try: 
            document = self.get_object() 
            serializer = self.get_serializer(document) 
            
            return Response(serializer.data) 
        except Document.DoesNotExist: 
            raise NotFound(
                detail="Document not found", 
                code=status.HTTP_404_NOT_FOUND
            )

    # Full Update (PUT) 
    def update(self, request, pk=None):
        partial = False
        document = self.get_object()

        serializer = self.get_serializer(document, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        validated_data = serializer.validated_data

        if 'file' in validated_data:
            file = validated_data['file']
            file_type = file.content_type

            if file_type.startswith('application/'):
                file_type = file_type[len('application/'):]
            elif file_type.startswith('image/'):
                file_type = file_type[len('image/'):]
            
            unique_filename = get_unique_filename(file.name)
            file.name = unique_filename
            file_content = ContentFile(file.read())
            saved_path = default_storage.save(file.name, file_content)

            validated_data['file'] = saved_path
            validated_data['file_type'] = file_type

        if 'title' in validated_data:
            unique_filename = get_unique_filename(validated_data['title'])
            validated_data['title'] = unique_filename

        for key, value in validated_data.items():
            setattr(document, key, value)

        document.save()

        return Response(serializer.data)
    
    # Partial Update (PATCH) 
    def partial_update(self, request, pk=None):
        partial = True
        document = self.get_object()

        serializer = self.get_serializer(document, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        validated_data = serializer.validated_data

        if 'file' in validated_data:
            file = validated_data['file']
            file_type = file.content_type

            if file_type.startswith('application/'):
                file_type = file_type[len('application/'):]
            elif file_type.startswith('image/'):
                file_type = file_type[len('image/'):]

            unique_filename = get_unique_filename(file.name)
            file.name = unique_filename
            file_content = ContentFile(file.read())
            saved_path = default_storage.save(file.name, file_content)

            validated_data['file'] = saved_path
            validated_data['file_type'] = file_type

        if 'title' in validated_data:
            unique_filename = get_unique_filename(validated_data['title'])
            validated_data['title'] = unique_filename

        for key, value in validated_data.items():
            setattr(document, key, value)

        document.save()

        return Response(serializer.data)

    # Delete (DELETE)
    def destroy(self, request, pk=None): 
        document = self.get_object() 
        document.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )