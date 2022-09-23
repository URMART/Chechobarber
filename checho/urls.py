from django.urls import path
from . import views

app_name='checho'

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('ingresar/', views.ingresar,name='ingresar'),
    path('cerraSesion/', views.cerraSesion,name='cerraSesion'),



#Datos de usuario----------------------------->

    path('registrarUser/', views.registrarUser,name='registrarUser'),
    path('guardarUser/', views.guardarUser,name='guardarUser'),
    path('listarClientes/', views.listarClientes,name='listarClientes'),
    path('eliminarCliente/<int:id>', views.eliminarCliente,name='eliminarCliente'),
    path('editarCliente/<int:id>', views.editarCliente,name='editarCliente'),
    path('guardarCliente/', views.guardarCliente,name='guardarCliente'),
    path('clientesBuscar/', views.clientesBuscar,name='clientesBuscar'),

    




#Datos del admin----------------------------->
    path('registrarAdmin/', views.registrarAdmin,name='registrarAdmin'),
    path('guardarAdmin/', views.guardarAdmin,name='guardarAdmin'),
    path('listarAdmin/', views.listarAdmin,name='listarAdmin'),
    path('eliminarAdmin/<int:id>', views.eliminarAdmin,name='eliminarAdmin'),
    path('editarAdmin/<int:id>', views.editarAdmin,name='editarAdmin'),
    path('guardadoAdmin/', views.guardadoAdmin,name='guardadoAdmin'),
    path('loginAdmin/', views.loginAdmin,name='loginAdmin'),
    path('logearAdmin/', views.logearAdmin,name='logearAdmin'),


    
    
    




#datos de empleado----------------------------->
    path('registrarEmpleado/', views.registrarEmpleado,name='registrarEmpleado'),
    path('guardarEmpleado/', views.guardarEmpleado,name='guardarEmpleado'),
    path('listarEmpleados/', views.listarEmpleados,name='listarEmpleados'),
    path('eliminarEmpleado/<int:id>', views.eliminarEmpleado,name='eliminarEmpleado'),
    path('editarEmpleado/<int:id>', views.editarEmpleado,name='editarEmpleado'),
    path('guardadoEmpleado/', views.guardadoEmpleado,name='guardadoEmpleado'),




#Datos Se Servicios -------------------------------->
path('registrarServicio/', views.registrarServicio,name='registrarServicio'),
path('guardarServicio/', views.guardarServicio,name='guardarServicio'),
path('listarServicios/', views.listarServicios,name='listarServicios'),
path('editarServicio/<int:id>', views.editarServicio,name='editarServicio'),
path('guardarEdicionServicio/', views.guardarEdicionServicio,name='guardarEdicionServicio'),
path('eliminarServicio/<int:id>', views.eliminarServicio,name='eliminarServicio'),
    


#Datos Citas
path('agendarCita/', views.agendarCita,name='agendarCita'),
path('guardarCita/', views.guardarCita,name='guardarCita'),
path('listarCita/', views.listarCita,name='listarCita'),
path('eliminarCita/<int:id>', views.eliminarCita,name='eliminarCita'),








]
