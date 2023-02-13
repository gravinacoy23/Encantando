from django import forms
from datetime import date

from employees.models import (
    EmployeesInfo, 
)

class CreateForm(forms.ModelForm):
    class Meta: 
        model = EmployeesInfo
        fields = (
            'employee_number',
            'nombre_completo',
            'fecha_de_nacimiento',
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
        widgets = {
            'fecha_de_nacimiento' : forms.SelectDateWidget(years=range(1970, date.today().year+10))
            }

        def clean_date(self):
                fecha = self.cleaned_date['date_of_birth']
                if fecha < date.today():
                    raise forms.ValidationError("The date cannot be in the past!")
                return date   

class UpdateContactForm(forms.ModelForm):
    class Meta: 
        model = EmployeesInfo
        fields = (
            'nombre_completo',
            'fecha_de_nacimiento',
            'cédula',
            'dirección',
            'celular',
            'correo_electrónico',
        )
        widgets = {
            'fecha_de_nacimiento' : forms.SelectDateWidget(years=range(1970, date.today().year+10))
            }

        def clean_date(self):
                fecha = self.cleaned_date['fecha_de_nacimiento']
                if fecha < date.today():
                    raise forms.ValidationError("The date cannot be in the past!")
                return date   

class UpdatePaymentsForm(forms.ModelForm):
    class Meta: 
        model = EmployeesInfo
        fields = (
            'método_de_pago',
            'número_de_cuenta',
            'declarante_de_renta',
            'EPS',
        )

class UpdateDocumentsForm(forms.ModelForm):
    class Meta: 
        model = EmployeesInfo
        fields = (
            'foto',
            'fotocopia_cédula',
            'carnet_EPS',
            'rut',
        )