from django.db import models
from django.urls import reverse

# Create your models here.

class Employees(models.Model):

    DECLARACION = (
    ('Si', 'Si'),
    ('No', 'No'),
    )

    METODOS = (
    ('Cuenta Bancaria', 'Cuenta Bancaria'), 
    ('Nequi', 'Nequi'),
    )

    EPS = (
    ('Aliansalud', 'Aliansalud'),
    ('Cafam EPS', 'Cafam EPS'),
    ('Capital Salud EPS', 'Capital Salud EPS'),
    ('Capresoca', 'Capresoca'),
    ('Colsubsidio', 'Colsubsidio'),
    ('COMFANDI', 'COMFANDI'),
    ('Compensar', 'Compensar'),
    ('Coomeva', 'Coomeva'),
    ('Coosalud', 'Coosalud'),
    ('EPS Sanitas', 'EPS Sanitas'),
    ('EPS Sura', 'EPS Sura'),
    ('Famisanar', 'Famisanar'),
    ('Medimás', 'Medimás'),
    ('Mutual SER', 'Mutual SER'),
    ('Nueva EPS', 'Nueva EPS'),
    ('Salud Total', 'Salud Total'),
    ('Savia Salud EPS', 'Savia Salud EPS'),
    ('SISBEN IV', 'SISBEN IV'),
    )

    FONDOS = (
    ('Colfondos', 'Colfondos'),
    ('Porvenir', 'Porvenir'),
    ('Protección', 'Protección'),
    ('Skandia', 'Skandia'),
    ('Colpensiones', 'Colpensiones'),
    )

    DOCUMENTOS = (
        ('Cédula', 'Cédula'),
        ('Tarjeta de Identidad', 'Tarjeta de identidad')
    )

    employee_number = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50)
    edad = models.IntegerField(default=18)
    cédula = models.CharField(max_length=30)
    dirección = models.CharField(max_length=100)
    celular = models.CharField(max_length=30)
    correo_electrónico = models.EmailField()
    declarante_de_renta = models.CharField(max_length=20, choices=DECLARACION, default='No')
    método_de_pago = models.CharField(max_length=20, choices=METODOS, default='Nequi')
    número_de_cuenta = models.CharField(max_length=50)
    EPS = models.CharField(max_length=20, choices=EPS, default='Aliansalud')
    foto = models.ImageField(blank=True, null=True, upload_to='static/media/employee_photos/%Y/%m/%D/')
    fotocopia_cédula = models.FileField(blank = True, null = True, upload_to='static/media/cedulas/%Y/%m/%D/')
    carnet_EPS = models.FileField(blank = True, null = True, upload_to='static/media/carnets/%Y/%m/%D/')
    rut = models.FileField(blank=True, null=True, upload_to='static/media/ruts/%Y/%m/%D/')

    class Meta:
        db_table = 'employees'
    
    def get_absolute_url(self):
        return reverse("lista_empleados", kwargs={"pk": self.employee_number})

    def __str__(self):
        return f'{self.nombre}'