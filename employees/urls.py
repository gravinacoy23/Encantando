from django.contrib import admin
from django.urls import path, re_path
from employees.views import EmployeeCreate, EmployeeList, EmployeeDetail, EmployeeUpdate


urlpatterns = [
    path('crear_empleado/', EmployeeCreate.as_view(), name = 'createemp'),
    path('lista_empleados', EmployeeList.as_view(), name = 'listemp'),
    path('detalle_empleado/<int:pk>', EmployeeDetail.as_view(), name = 'showemp'),
    path('actualizar_empleado/<int:pk>', EmployeeUpdate.as_view(), name = 'updateemp'),
]  