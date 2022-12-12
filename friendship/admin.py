from django.contrib import admin

from .models import Categoria, Incidentes, Centros
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Incidentes) 
admin.site.register(Centros)