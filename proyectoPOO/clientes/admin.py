from django.contrib import admin


from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ("nombre", "apellido", "email", "telefono", "direccion")
	search_fields = ("nombre", "apellido", "email")
