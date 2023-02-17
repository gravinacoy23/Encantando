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

from artistas.models import Employees
from artistas.forms import (
    CreateForm,
    UpdatePaymentsForm,
    UpdateDocumentsForm,
    UpdateContactForm,
)

# Create your views here.

class EmployeeCreate(CreateView):
    form_class = CreateForm
    template_name = 'employeeCreate.html'
    success_url = reverse_lazy('listemp')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class EmployeeList(ListView):
    model = Employees
    template_name = 'employeeList.html'
    success_url = reverse_lazy('listemp')
    

class EmployeeDetail(DetailView):
    model = Employees
    template_name = 'employeeDetail.html'
    
    def get_success_url(self):
        return reverse('showemp', args=(self.kwargs['pk'],))

class EmployeeDetailContact(DetailView):
    model = Employees
    template_name = 'employeeDetailContact.html'
    
    def get_success_url(self):
        return reverse('showcontact', args=(self.kwargs['pk'],))

class EmployeeUpdateContact(UpdateView):
    form_class = UpdateContactForm
    model = Employees
    template_name = 'employeeDetailContact_update.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('showemp', args=(self.kwargs['pk'],))

class EmployeeDetailPagos(DetailView):
    model = Employees
    template_name = 'employeeDetailPayments.html'
    
    def get_success_url(self):
        return reverse('showpaymentinfo', args=(self.kwargs['pk'],))

class EmployeeUpdatePayments(UpdateView):
    form_class = UpdatePaymentsForm
    model = Employees
    template_name = 'employeeDetailPayments_update.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('showpaymentinfo', args=(self.kwargs['pk'],))

class EmployeeDetailDocuments(DetailView):
    model = Employees
    template_name = 'employeeDetailDocuments.html'
    
    def get_success_url(self):
        return reverse('', args=(self.kwargs['pk'],))

class EmployeeUpdateDocuments(UpdateView):
    form_class = UpdateDocumentsForm
    model = Employees
    template_name = 'employeeDetailDocuments_update.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('showpaymentinfo', args=(self.kwargs['pk'],))