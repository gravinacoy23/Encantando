from django.contrib import admin
from django.urls import path, re_path
from artistas.views import (
    EmployeeCreate,
    EmployeeList,
    EmployeeDetail, 
    EmployeeDetailContact,
    EmployeeUpdateContact, 
    EmployeeDetailPagos, 
    EmployeeUpdatePayments,
    EmployeeDetailDocuments,
    EmployeeUpdateDocuments,
)


urlpatterns = [
    path('crear_empleado/', EmployeeCreate.as_view(), name = 'createemp'),
    path('lista_empleados', EmployeeList.as_view(), name = 'listemp'),
    path('detalle_empleado/<int:pk>', EmployeeDetail.as_view(), name = 'showemp'),
    path('detalle_empleado/contacto/<int:pk>', EmployeeDetailContact.as_view(), name = 'showcontact'),
    path('detalle-empleado/contacto/actualizar/<int:pk>', EmployeeUpdateContact.as_view(), name = 'updatecontact'),
    path('detalle_empleado/pagos/<int:pk>', EmployeeDetailPagos.as_view(), name = 'showpaymentinfo'),
    path('detalle_empleado/pagos/actualizar/<int:pk>', EmployeeUpdatePayments.as_view(), name = 'updatepaymentinfo'),
    path('detalle_empleado/documentos/<int:pk>', EmployeeDetailDocuments.as_view(), name = 'showdocuments'),
    path('detalle_empleado/documentos/actualizar/<int:pk>', EmployeeUpdateDocuments.as_view(), name = 'updatedocuments'),
]  
