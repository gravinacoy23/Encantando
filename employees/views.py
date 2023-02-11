from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)   

from employees.models import EmployeesInfo
from employees.forms import EmployeeForm

# Create your views here.

class EmployeeCreate(CreateView):
    form_class = EmployeeForm
    template_name = 'employeeCreate.html'
    success_url = reverse_lazy('listemp')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class EmployeeList(ListView):
    model = EmployeesInfo
    template_name = 'employeeList.html'
    success_url = reverse_lazy('listemp')
    

class EmployeeDetail(DetailView):
    model = EmployeesInfo
    template_name = 'employeeDetail.html'
    
    def get_success_url(self):
        return reverse('showemp', args=(self.kwargs['pk'],))


class EmployeeUpdate(UpdateView):
    form_class = EmployeeForm
    model = EmployeesInfo
    template_name = 'employeeUpdate.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('updateemp', args=(self.kwargs['pk'],))