# poblar_datos.py
from biblioteca.models import Autor, Libro, Resena
import datetime

# (Opcional) Limpiar datos anteriores
Autor.objects.all().delete()
Libro.objects.all().delete()
Resena.objects.all().delete()

autor1 = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombiana")
autor2 = Autor.objects.create(nombre="Isabel Allende",    nacionalidad="Chilena")

libro1 = Libro.objects.create(
    titulo="Cien años de soledad",
    autor=autor1,
    fecha_publicacion=datetime.date(1967, 6, 5),
    resumen="Novela emblemática del realismo mágico, que narra la historia de la familia Buendía durante varias generaciones."
)
# … más libros …

Resena.objects.create(libro=libro1, texto="Una obra maestra de la literatura universal.", calificacion=5)
# … más reseñas …

print("Datos poblados exitosamente.")
