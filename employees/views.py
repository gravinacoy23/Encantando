from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from . models import EmployeesInfo

# Create your views here.

class EmployeeCreate(CreateView):
    model = EmployeesInfo
    fields = '__all__'
    template_name = 'employeeCreate.html'
    success_url = '/listaempleados/'

class EmployeeList(ListView):
    model = EmployeesInfo
    template_name = 'employeeList.html'
    success_url = 'listaempleados/exitoso'
    

class EmployeeDetail(DetailView):
    model = EmployeesInfo
    template_name = 'employeeDetail.html'
    success_url = 'detalle-empleado/exitoso'


class EmployeeUpdate(UpdateView):
    model = EmployeesInfo
    fields = '__all__'
    template_name = 'employeeUpdate.html'
    success_url = '/listaempleados/'