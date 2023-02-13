from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import date 

# Create your models here.

class EmployeesInfo(models.Model):

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

    employee_number = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField(default = timezone.now)
    cédula = models.CharField(max_length=30)
    dirección = models.CharField(blank = True, max_length=100)
    celular = models.CharField(max_length=30)
    correo_electrónico = models.EmailField()
    declarante_de_renta = models.CharField(max_length=20, choices=DECLARACION, default='No')
    método_de_pago = models.CharField(max_length=20, choices=METODOS, default='Nequi')
    número_de_cuenta = models.CharField(max_length=50)
    EPS = models.CharField(max_length=20, choices=EPS, default='Aliansalud')
    foto = models.ImageField(blank=True, null=True, upload_to='employee_photos/%Y/%m/%D/')
    fotocopia_cédula = models.FileField(blank = True, null = True, upload_to='cedulas/%Y/%m/%D/')
    carnet_EPS = models.FileField(blank = True, null = True, upload_to='carnets/%Y/%m/%D/')
    rut = models.FileField(blank=True, null=True, upload_to='ruts/%Y/%m/%D/')

    class Meta:
        db_table = 'employeesInfo'
    
    def get_age(self):
        age = date.today() - self.fecha_de_nacimiento
        return int((age).days/365.25)

    def get_absolute_url(self):
        return reverse("lista_empleados", kwargs={"pk": self.employee_number})

    def __str__(self):
        return f'{self.nombre_completo}'