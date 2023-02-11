from django.contrib import admin
from django.urls import path
from . views import EmployeeCreate, EmployeeList, EmployeeDetail


urlpatterns = [
    path('crearemp/', EmployeeCreate.as_view(), name = 'createmp'),
    path('listaempleados', EmployeeList.as_view(), name = 'listemp'),
    path('detalle_empleado/<int:pk>', EmployeeDetail.as_view(), name = 'showemp')
]
