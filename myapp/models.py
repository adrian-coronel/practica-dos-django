# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autor(models.Model):
    idautor = models.AutoField(db_column='idAutor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100, blank=True, null=True)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self) -> str:
            return self.nombre
    class Meta:
        managed = False
        db_table = 'autor'


class Libro(models.Model):
    idlibro = models.AutoField(db_column='idLibro', primary_key=True)  # Field name made lowercase.
    idautor = models.ForeignKey(Autor, models.DO_NOTHING, db_column='idAutor')  # Field name made lowercase.
    codigo = models.PositiveIntegerField(unique=True, blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    editorial = models.CharField(max_length=60, blank=True, null=True)
    numpages = models.PositiveIntegerField(db_column='numPages', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.titulo
    class Meta:
        managed = False
        db_table = 'libro'


class Prestamo(models.Model):
    idprestamo = models.AutoField(db_column='idPrestamo', primary_key=True)  # Field name made lowercase.
    idlibro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='idLibro')  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    fecprestamo = models.DateTimeField(db_column='fecPrestamo', blank=True, null=True)  # Field name made lowercase.
    fecdevolucion = models.DateTimeField(db_column='fecDevolucion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prestamo'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    numusuario = models.PositiveIntegerField(db_column='numUsuario')  # Field name made lowercase.
    nif = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self) -> str:
            return self.nombre
    class Meta:
        managed = False
        db_table = 'usuario'
