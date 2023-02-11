from django import forms

from employees.models import EmployeesInfo

class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = EmployeesInfo
        fields = '__all__'
