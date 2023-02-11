from django.db import models
from django.urls import reverse

# Create your models here.
class EmployeesInfo(models.Model):
    employee_number = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(blank = True, max_length=50)
    cédula = models.CharField(blank = True, max_length=30)
    celular = models.CharField(blank = True, max_length=30)
    corre_electrónico = models.EmailField(blank = True)
    talla_zapatos = models.IntegerField(blank = True)
    foto = models.ImageField(blank=True, null=True, upload_to='employee_photos/%Y/%m/%D/')
    rut = models.FileField(blank=True, null=True, upload_to='ruts/%Y/%m/%D/')

    class Meta:
        db_table = 'EmployeesInfo'
    
    def __str__(self):
        return f'{self.nombre_completo}'
    
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})