from django.contrib import admin
from django.urls import path
from . views import EmployeeCreate, EmployeeList, EmployeeDetail, EmployeeUpdate


urlpatterns = [
    path('crear_empleado/', EmployeeCreate.as_view(), name = 'createmp'),
    path('lista_empleados', EmployeeList.as_view(), name = 'listemp'),
    path('detalle_empleado/<int:pk>', EmployeeDetail.as_view(), name = 'showemp'),
    path('actualizar_empleados/<int:pk>', EmployeeUpdate.as_view(), name = 'updateemployee'),
]
