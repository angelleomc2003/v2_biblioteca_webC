from rest_framework import serializers
from .models import Libro, Review, Autor 

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'texto', 'rating', 'fecha']

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='autor.nombre')
    recent_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = [
            'id', 'titulo', 'autor', 'author_name',
            'fecha_publicacion', 'resumen', 'recent_reviews'
        ]

    def get_recent_reviews(self, obj):
        # usa el related_name 'resenas_review'
        qs = obj.resenas_review.order_by('-fecha')[:5]
        return ReviewSerializer(qs, many=True).data
