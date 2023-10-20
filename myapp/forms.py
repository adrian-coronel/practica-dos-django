from django.forms import ModelForm
from .models import *


class LibroForm(ModelForm):
  class Meta:
    model= Libro
    fields= '__all__'
class PrestamoForm(ModelForm):
  class Meta:
    model= Prestamo
    fields= '__all__'
    
class UsuarioForm(ModelForm):
  class Meta:
    model= Usuario
    fields= '__all__'
class AutorForm(ModelForm):
  class Meta:
    model= Autor
    fields= '__all__'