# Proyecto Django CRUD de Clientes

Este proyecto tiene un CRUD para la gestión de clientes usando Django, SQLite y Bootstrap 5. Se aplica Programación Orientada a Objetos (POO) en la definición y uso del modelo `Cliente`.

## POO

La Programación Orientada a Objetos se aplica en Django a través de la definición de modelos como clases Python. En este proyecto, la clase `Cliente` representa el objeto principal del sistema y encapsula sus atributos y comportamientos.

### Estructura de la clase `Cliente`

```python
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
```

- **Atributos:** Cada campo de la clase es un atributo del objeto `Cliente`.
- **Métodos:** El método `__str__` define cómo se representa el objeto como texto.
- **Instanciación:** Cada registro en la base de datos es una instancia de la clase `Cliente`.

## Estructura del Proyecto

- `clientes/models.py`: Definición de la clase `Cliente` (POO).
- `clientes/forms.py`: Formulario basado en el modelo `Cliente`.
- `clientes/views.py`: Vistas CRUD para el modelo.
- `clientes/templates/`: Templates con Bootstrap 5 para la interfaz.
- `clientes_project/settings.py`: Configuración del proyecto.

## Ejecución

1. Instala dependencias y activa el entorno virtual.
2. Ejecuta migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```
4. Accede a `http://127.0.0.1:8000/` para usar la app.

---

<img width="1153" height="432" alt="image" src="https://github.com/user-attachments/assets/38ac4443-a31a-4e92-8da6-29a065e97b99" />
<img width="556" height="610" alt="image" src="https://github.com/user-attachments/assets/cc25fed1-5ccb-41b6-bf69-6938e2610fa5" />
<img width="869" height="284" alt="image" src="https://github.com/user-attachments/assets/4dd11024-6c78-4899-a7cd-9b4ff1914d0f" />
<img width="556" height="610" alt="image" src="https://github.com/user-attachments/assets/9d86a3f9-d6c3-4929-ac03-b993b657b40b" />


