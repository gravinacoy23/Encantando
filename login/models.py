from django.db import models
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, blank= True, null = True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    correo_electrónico = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return f'{self.nombre}'