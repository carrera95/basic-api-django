from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.response import Response
from rest_framework import status

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        documents = self.get_queryset() 
        serializer = self.get_serializer(documents, many=True) 
        
        return Response(serializer.data)

    def create(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        self.perform_create(serializer) 
        headers = self.get_success_headers(serializer.data) 
        
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )

    def retrieve(self, request, pk=None):
        pass
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass