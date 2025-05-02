from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import Autor, Libro, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['autor', 'fecha_publicacion']
    ordering_fields = ['fecha_publicacion', 'titulo']

    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        libro = self.get_object()
        avg = libro.resenas.aggregate(avg=Avg('rating'))['avg'] or 0
        return Response({'average_rating': avg})

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer