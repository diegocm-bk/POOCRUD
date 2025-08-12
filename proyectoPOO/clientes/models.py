from django.db import models


class Cliente(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	telefono = models.CharField(max_length=20, blank=True)
	direccion = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return f"{self.nombre} {self.apellido}"
