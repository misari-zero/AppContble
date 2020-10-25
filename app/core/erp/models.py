from datetime import datetime

from django.db import models



# class Type(models.Model):
#     cod = models.CharField(max_length=2, verbose_name='Tipo de cliente')
#     name = models.CharField(max_length=150, verbose_name='Nombre')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Tipo'
#         verbose_name_plural = 'Tipos'
#         db_table = 'tipo_cli'
#         ordering = ['id']
from django.forms import model_to_dict


class Client(models.Model):
    # type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombres o Razon social')
    address = models.CharField(max_length=150, verbose_name='Direccion')
    ruc = models.CharField(max_length=11, unique=True, verbose_name='Ruc')
    fecha = models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_created = models.DateTimeField(auto_now=True)
    fecha_updated = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres o Razon social')
    desc = models.CharField(max_length=150, verbose_name='Descripcion')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    fecha = models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_created = models.DateTimeField(auto_now=True)
    fecha_updated = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Factura(models.Model):
    fecha_emision = models.DateField(default=datetime.now)
    fecha_venc = models.DateField(blank=True, null=True)
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    pro = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    cantidad = models.IntegerField(default=0)
    pre = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    igv = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.name

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ['id']



# class Comprobante(models.Model):
#     tipo = models.CharField(max_length=2, verbose_name='Tipo de comprobante', unique=True)
#     name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Comprobante'
#         verbose_name_plural = 'Comprobantes'
#         db_table = 'tipo_com'
#         ordering = ['id']

# class Serie(models.Model):
#     cod = models.OneToOneField(Comprobante, on_delete=models.CASCADE)
#     nro_serie = models.CharField(max_length=6, verbose_name='Numero de serie', unique=True)
#     numero = models.CharField(max_length=150, verbose_name='Numero de documento', unique=True)
#
#     def __str__(self):
#         return self.serie
#
#     class Meta:
#         verbose_name = 'Serie'
#         verbose_name_plural = 'Series'
#         db_table = 'nro_serie'
#         ordering = ['id']

# class Sale(models.Model):
#     fecha_emision = models.DateField(default=datetime.now)
#     fecha_venc = models.DateField(blank=True, null=True)
#     cli = models.ForeignKey(Client, on_delete=models.CASCADE)
#     date_joined = models.DateField(default=datetime.now)
#     subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     igv = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#
#     def __str__(self):
#         return self.cli.name
#
#     class Meta:
#         verbose_name = 'Venta'
#         verbose_name_plural = 'Ventas'
#         ordering = ['id']