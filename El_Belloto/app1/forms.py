from django import forms
from .models import Pendiente

class PendienteForm(forms.ModelForm):
    class Meta:
        model = Pendiente
        fields = ('categoria_pendiente', 'descripcion_pendiente', 'tiempo_destinado')

