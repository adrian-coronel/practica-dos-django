from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from datetime import datetime

#Import models
from .models import *
from .forms import *

# Create your views here.
class PrestamoView(View):

  def get(self, request):
    listaPrestamos = Prestamo.objects.all()

    context = {
      'prestamos': listaPrestamos,
    }
    return render(request, 'index.html', context)

class FormSaveView(View):
  
  def get(self, request):
    form = PrestamoForm()
    context = {
      'form': form
    }

    return render(request, 'create.html', context)


  def post(self, request):
      idLibro= request.POST['idlibro']
      idUsuario= request.POST['idusuario']
      fecPrestamo= request.POST['fecprestamo']
      fecDevolucion= request.POST['fecdevolucion']
      
      libro= Libro.objects.get(idlibro= idLibro)
      usuario= Usuario.objects.get(idusuario= idUsuario)

      newPrestamo= Prestamo(
        idlibro= libro,
        idusuario= usuario,
        fecprestamo= fecPrestamo,
        fecdevolucion= fecDevolucion
      )
      newPrestamo.save();
      
      return redirect('/')

class FormUpdateView(View):
  
  def get(self, request, id):
    prestamo= Prestamo.objects.get(idprestamo= id)
    usuarios= Usuario.objects.all()
    libros= Libro.objects.all()

    context= {
      'prestamo': prestamo,
      'usuarios': usuarios,
      'libros': libros
    }

    return render(request, 'edit.html', context)

  def post(self, request, id):
    idLibro= request.POST['idlibro']
    idUsuario= request.POST['idusuario']
    fecPrestamo= request.POST['fecprestamo']
    fecDevolucion= request.POST['fecdevolucion']
    
    libro= Libro.objects.get(idlibro= idLibro)
    usuario= Usuario.objects.get(idusuario= idUsuario)

    updatedPrestamo= Prestamo.objects.get(idprestamo= id)
    updatedPrestamo.idlibro= libro
    updatedPrestamo.idusuario= usuario
    updatedPrestamo.fecprestamo= fecPrestamo
    updatedPrestamo.fecdevolucion= fecDevolucion
    updatedPrestamo.save()

    return redirect('/')

class DeletePrestamoView(View):
  def post(self, request):
    id= request.POST['idprestamo']
    deletedPrestamo= Prestamo.objects.get(idprestamo= id)
    deletedPrestamo.delete()

    return redirect('/')