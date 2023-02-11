from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from . models import EmployeesInfo

# Create your views here.

class EmployeeCreate(CreateView):
    model = EmployeesInfo
    fields = '__all__'
    template_name = 'employeeCreate.html'
    success_url = '/crearemp/exitoso/'

class EmployeeList(ListView):
    model = EmployeesInfo
    success_url = 'listaempleados/exitoso'
    template_name = 'employeeList.html'

class EmployeeDetail(ListView):
    model = EmployeesInfo
    success_url = 'detalle-empleado/exitoso'
    template_name = 'employeeDetail.html'