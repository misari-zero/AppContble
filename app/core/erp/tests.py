from app.wsgi import *
from core.erp.models import Client

# Listar

# select * from Tabla
query = Client.objects.all()
print(query)

# insercion
c = Client()
c.name = 'Jorgito'
c.address = 'Av Cultura'
c.ruc = '10710501063'
c.fecha = '2020-10-22 01:14:01.245441'
c.fecha_created = '2020-10-22 01:14:01.245441'
fecha_updated = '2020-10-22 01:14:01.245441'
c.save()