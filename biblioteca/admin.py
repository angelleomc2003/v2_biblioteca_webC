from django.contrib import admin
from .models import Autor, Libro, Resena

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo',)
    list_filter = ('fecha_publicacion',)

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('id', 'libro', 'calificacion', 'fecha')
    search_fields = ('libro__titulo',)
    list_filter = ('calificacion', 'fecha')