from django.db import models
from datetime import datetime
from django.forms import model_to_dict, TextInput

from app.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import mes_choices, ano_choices

from django.forms import model_to_dict


class Client(models.Model):
    # type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombres o Razon social')
    address = models.CharField(max_length=150, verbose_name='Direccion')
    ruc = models.CharField(max_length=11, unique=True, verbose_name='Ruc')
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    # gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']

class Elemento(models.Model):
    nro = models.CharField(max_length=2, verbose_name='Número elemento', unique=True)
    name = models.CharField(max_length=120, verbose_name='Nombre de elemento')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'
        ordering = ['id']


class Tipocuenta(models.Model):
    codigo = models.CharField(max_length=2, verbose_name='Código', unique=True)
    name = models.CharField(max_length=120, verbose_name='Nombre')
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipocuenta'
        verbose_name_plural = 'Tipocuentas'
        ordering = ['id']


class Plancontable(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre')
    tipo = models.ForeignKey(Tipocuenta, on_delete=models.CASCADE, verbose_name='Tipo cuenta')
    cta = models.CharField(max_length=7, verbose_name='CTA', unique=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['id']


# class AsientoContable(models.Model):
#     nro = models.IntegerField()
#     ano = (('2020'), ('2021'), ('2022'), ('2023'), ('2024'), ('2025'))
#     mes = (('ENERO'), ('FEBRERO'), ('MARZO'), ('ABRIL'), ('MAYO'), ('JUNIO'), ('JUlIO'), ('AGOSTO'), ('SEPTIEMBRE'), ('OCTUBRE'), ('NOVIEMBRE'), ('DICIEMBRE'))
#     cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE, verbose_name='CUENTA')
#     detalle = models.CharField(max_length=120, verbose_name='DETALLE DE CUENTA')
#     debe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='DEBE')
#     haber = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='HABER')
#     subtotal1 = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='SUBTOTAL1')
#     subtotal2 = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='SUBTOTAL2')
#
#     def __str__(self):
#         return self.cuenta
#
#     class Meta:
#         verbose_name = 'Asiento'
#         verbose_name_plural = 'Asientos'
#         ordering = ['id']
#


class Categoria(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, blank=True, null=True, verbose_name='Descripción')
    codi = models.ForeignKey(Plancontable, on_delete=models.CASCADE, verbose_name='Nombre cuenta')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    cate = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    desc = models.CharField(max_length=150, verbose_name='Descripcion', null=True, blank=True)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    fecha = models.DateTimeField(default=datetime.now, verbose_name='Fecha de registro')
    state = models.BooleanField(default=True, verbose_name='Estado')

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


# class Factura(models.Model):
#     fecha_emision = models.DateField(default=datetime.now)
#     fecha_venc = models.DateField(blank=True, null=True)
#     cli = models.ForeignKey(Client, on_delete=models.CASCADE)
#     pro = models.ForeignKey(Product, on_delete=models.CASCADE)
#     date_joined = models.DateField(default=datetime.now)
#     cantidad = models.IntegerField(default=0)
#     pre = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     igv = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#
#     def __str__(self):
#         return self.cli.name
#
#     class Meta:
#         verbose_name = 'Factura'
#         verbose_name_plural = 'Facturas'
#         ordering = ['id']
#
#
# class Tipodoc(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nombre')
#     ref = models.CharField(max_length=6, verbose_name='Nro Serie')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Tipodoc'
#         verbose_name_plural = 'Tipodocs'
#         db_table = 'tipo_doc'
#         ordering = ['id']
#
#
# class Compra(models.Model):
#     cod = models.DecimalField(default=1401, max_digits=4, decimal_places=0)
#     doc = models.ForeignKey(Tipodoc, on_delete=models.CASCADE)
#     ctaabono = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
#     nro = models.CharField(max_length=13, verbose_name='Numero')
#     fecha_emi = models.DateField(default=datetime.now)
#     cli = models.ForeignKey(Client, on_delete=models.CASCADE)
#     subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#
#     def __str__(self):
#         return self.cli.name
#
#     class Meta:
#         verbose_name = 'Compra'
#         verbose_name_plural = 'Compras'
#         ordering = ['id']
#
#
# class Detcomprobanteingreso(models.Model):
#     comingreso = models.ForeignKey(Comprobanteingreso, on_delete=models.CASCADE)
#     cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
#     debe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     haber = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#
#     def __str__(self):
#         return self.cuenta.name
#
#     class Meta:
#         verbose_name = 'Detcomprobanteingreso'
#         verbose_name_plural = 'Detcomprobanteingresos'
#         ordering = ['id']


class Diario(models.Model):
    nro = models.IntegerField()
    ano = models.CharField(max_length=10, choices=ano_choices, default='2020', verbose_name='Año')
    mes = models.CharField(max_length=10, choices=mes_choices, default='NOVIEMBRE', verbose_name='Mes')
    date_joined = models.DateField(default=datetime.now)
    cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
    desc = models.CharField(max_length=50)
    debe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    haber = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    impuestos = models.CharField(max_length=3)

    def __str__(self):
        return self.desc

    def toJSON(self):
        item = model_to_dict(self)
        item['ano'] = {'id': self.ano, 'name': self.get_ano_display()}
        item['mes'] = {'id': self.mes, 'name': self.get_mes_display()}
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['cuenta'] = self.cuenta.toJSON()
        # item['desc'] = self.desc.toJSON()
        # item['debe'] = format(self.debe, '.2f')
        # item['haber'] = format(self.haber, '.2f')
        # item['impuestos'] = self.impuestos.toJSON()
        return item

    class Meta:
        verbose_name = 'Diario'
        verbose_name_plural = 'Diarios'
        ordering = ['id']


class Egreso(models.Model):
    nro = models.IntegerField()
    ano = models.CharField(max_length=10, choices=ano_choices, default='2020', verbose_name='Año')
    mes = models.CharField(max_length=10, choices=mes_choices, default='NOVIEMBRE', verbose_name='Mes')
    date_joined = models.DateField(default=datetime.now)
    cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
    desc = models.CharField(max_length=50)
    debe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    haber = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    impuestos = models.CharField(max_length=3)

    def __str__(self):
        return self.desc

    def toJSON(self):
        item = model_to_dict(self)
        item['ano'] = {'id': self.ano, 'name': self.get_ano_display()}
        item['mes'] = {'id': self.mes, 'name': self.get_mes_display()}
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['cuenta'] = self.cuenta.toJSON()
        # item['desc'] = self.desc.toJSON()
        # item['debe'] = format(self.debe, '.2f')
        # item['haber'] = format(self.haber, '.2f')
        # item['impuestos'] = self.impuestos.toJSON()
        return item

    class Meta:
        verbose_name = 'Egreso'
        verbose_name_plural = 'Egresos'
        ordering = ['id']


class Mayor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre diario')
    ano = models.CharField(max_length=10, choices=ano_choices, default='2020', verbose_name='Año')
    mes = models.CharField(max_length=10, choices=mes_choices, default='NOVIEMBRE', verbose_name='Mes')
    date_joined = models.DateField(default=datetime.now)
    # cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
    desc = models.CharField(max_length=50, verbose_name='Descripción')
    deudor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    acreedor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.desc

    def toJSON(self):
        item = model_to_dict(self)
        item['name'] = self.name.toJSON()
        item['ano'] = {'id': self.ano, 'name': self.get_ano_display()}
        item['mes'] = {'id': self.mes, 'name': self.get_mes_display()}
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['cuenta'] = self.cuenta.toJSON()
        # item['desc'] = self.desc.toJSON()
        # item['debe'] = format(self.debe, '.2f')
        # item['haber'] = format(self.haber, '.2f')
        # item['impuestos'] = self.impuestos.toJSON()
        return item

    class Meta:
        verbose_name = 'Egreso'
        verbose_name_plural = 'Egresos'
        ordering = ['id']

# class DetDiario(models.Model):
#     diario = models.ForeignKey(Diario, on_delete=models.CASCADE)
#     cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
#     debe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     haber = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#
#     def __str__(self):
#         return self.cuenta.name
#
#     def toJSON(self):
#         item = model_to_dict(self, exclude=['diario'])
#         item['cuenta'] = self.cuenta.toJSON()
#         item['debe'] = format(self.debe, '.2f')
#         item['haber'] = format(self.haber, '.2f')
#         return item
#
#     class Meta:
#         verbose_name = 'DetDiario'
#         verbose_name_plural = 'DetDiarios'
#         ordering = ['id']



