from django.contrib import admin

# Register your models here.
from .models import Pendiente, Empresa

admin.site.register(Pendiente)
admin.site.register(Empresa)