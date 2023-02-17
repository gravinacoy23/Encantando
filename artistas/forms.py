from django import forms
from datetime import date

from artistas.models import (
    Employees, 
)

class CreateForm(forms.ModelForm):
    class Meta: 
        model = Employees
        fields = (
            'employee_number',
            'nombre',
            'edad',
            'cédula',
            'dirección',
            'celular',
            'correo_electrónico',
            'declarante_de_renta',
            'método_de_pago',
            'número_de_cuenta',
            'EPS',
            'foto',
            'fotocopia_cédula',
            'carnet_EPS',
            'rut',
        ) 

class UpdateContactForm(forms.ModelForm):
    class Meta: 
        model = Employees
        fields = (
            'nombre',
            'edad',
            'cédula',
            'dirección',
            'celular',
            'correo_electrónico',
        )

class UpdatePaymentsForm(forms.ModelForm):
    class Meta: 
        model = Employees
        fields = (
            'método_de_pago',
            'número_de_cuenta',
            'declarante_de_renta',
            'EPS',
        )

class UpdateDocumentsForm(forms.ModelForm):
    class Meta: 
        model = Employees
        fields = (
            'foto',
            'fotocopia_cédula',
            'carnet_EPS',
            'rut',
        )