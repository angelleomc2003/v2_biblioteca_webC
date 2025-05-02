# 📚 Biblioteca API con Django REST Framework

Este repositorio contiene una aplicación Django extendida con Django REST Framework (DRF) para exponer una API RESTful de gestión de autores, libros y reseñas.

## 🎯 Objetivos

- Registrar y consultar autores y libros.
- Crear y gestionar reseñas con validaciones de rango.
- Exponer endpoints para filtrado, ordenamiento y paginación.
- Implementar campos computados y rutas personalizadas en la API.

## 🚀 Tecnologías

- Python 3.8+
- Django 5.2
- Django REST Framework
- django-filter

## 📂 Estructura del proyecto

```

biblioteca\_project/
│
├── biblioteca/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── filters.py      # (opcional)
│   └── urls.py
│
├── biblioteca\_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── poblar\_datos.py
├── manage.py
└── README.md

````

## 🔧 Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/angelleomc2003/v2_biblioteca_webC.git
   cd v2_biblioteca_webC
````

2. Crea y activa entorno virtual:

   ```bash
   python -m venv env
   # Windows:
   .\env\Scripts\activate
   # Linux/macOS:
   source env/bin/activate
   ```

3. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplica migraciones:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crea superusuario (opcional, para /admin):

   ```bash
   python manage.py createsuperuser
   ```

6. Pobla datos de prueba:

   ```bash
   python manage.py shell
   >>> exec(open('poblar_datos.py').read())
   ```

7. Levanta el servidor:

   ```bash
   python manage.py runserver
   ```

Accede a la API en `http://127.0.0.1:8000/api/`

## 📋 Endpoints Principales

* **Autores**

  * `GET /api/authors/`
  * `POST /api/authors/`
* **Libros**

  * `GET /api/books/`

    * Filtros: `?autor=<id>`
    * Orden: `?ordering=-fecha_publicacion`
    * Paginación: `?page=<n>`
  * `GET /api/books/{id}/average_rating/`
* **Reseñas**

  * `GET /api/reviews/`
  * `POST /api/reviews/`

## 📝 Notas Técnicas

* **`SerializerMethodField`** en `BookSerializer` para incluir las últimas 5 reseñas (`recent_reviews`).
* **django-filter** para filtros automáticos en `BookViewSet` (`filterset_fields`).
* **PageNumberPagination** con tamaño de página configurado en `settings.py`.
* **`@action(detail=True)`** para exponer ruta custom `average_rating`.