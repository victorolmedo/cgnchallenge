# cgnchallenge
#!/bin/bash

# Clonar el repositorio
git clone https://github.com/victorolmedo/cgnchallenge.git
cd tu-repositorio

# Configurar entorno virtual
python -m venv venv
source venv/bin/activate
# .ENV 
Copiar .env.example a .env:

# Instalar dependencias
pip install -r requirements.txt

# Restaurar la base de datos (PostgreSQL)
createdb ceragon
pg_restore -h localhost -U postgres -d ceragon dump-ceragon.dump

# Migraciones de Django
python manage.py migrate

# Carga inicial
python manage.py loaddata autores.json

# Luego cargar libros
python manage.py loaddata libros.json

# Crear superusuario (opcional)
python manage.py createsuperuser

# Iniciar el servidor
python manage.py runserver

# Annotate /  Aggregate / Filtros especiales 
Direction postman, un collection de los request 

