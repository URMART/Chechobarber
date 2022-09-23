from django.contrib import messages
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from  .models import *
from django.core.paginator import Paginator


# Create your views here.
#return HttpResponseRedirect(reverse('territorio:aprendiz'))
def index(request):
    return render(request, 'index.html')

# Datos del login ------------------------------------------------------
def login(request):
    return render(request, 'login/login.html')

def ingresar(request):
    if request.method == "POST":
        try:
            #capturar datos del formulario
            use = request.POST["usua"]
            pasw = request.POST["clave"]
            
            #verificar si existe en base de datos
            q = Clientes.objects.get(usuario = use, contraseña = pasw)
            
            #crear la variable de sesion
            request.session["logueo"] = [q.id,q.usuario,q.rol]

            return redirect('checho:index')
        except Clientes.DoesNotExist:
            messages.error(request, "Usuario o contraseña incorrectos...")
            return redirect('checho:login')
    else:
        messages.warning(request, "Usted no envió datos...")
        return redirect('checho:login')

def cerraSesion(request):
    try:
        del request.session["logueo"]
        messages.success(request, "Sesión cerrada correctamente!")
    except Exception as e:
        messages.error(request, "Ocurrió un error, intente de nuevo...")
    
    return redirect('checho:index')


#datos del usuario o cliente -------------------------------->
def registrarUser(request):
    return render(request, 'usuario/registrarUser.html')

def guardarUser(request):
    try:
        if request.method == 'POST':
            nom=request.POST['nombre']
            apell=request.POST['apellido']
            numTel=request.POST['telefono']
            user=request.POST['user']
            contra=request.POST['passw']

            q=Clientes.objects.create(nombre=nom,apellido=apell,numeroTelefono=numTel,usuario=user,contraseña=contra)
            messages.success(request, 'Cliente agregado')

            return  redirect('checho:listarClientes')
        else:
            
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarClientes') 
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarClientes')           
    

def listarClientes(request):
    q=Clientes.objects.all()
    pag = Paginator(q, 4)   #cinco registros por página
    page_number = request.GET.get('page')
        
        #sobreescribo el query
    q = pag.get_page(page_number)
        
    contexto = {'page_obj': q}
    return render(request,'usuario/listarUsuarios.html',contexto)


def eliminarCliente(request,id):
    try: 
        q=Clientes.objects.get(id=id)

        q.delete()
        messages.success(request, 'Cliente Eliminado')
        return redirect('checho:listarClientes') 
    except Exception as e:
        return HttpResponse(e)


def editarCliente(request,id):

    client=Clientes.objects.get(id=id)

    return render(request, 'usuario/edicionCliente.html',{'client':client})


def guardarCliente(request):

    try:
        if request.method == 'POST':
            nom=request.POST['nombre']
            ape=request.POST['apellido']
            tel=request.POST['telefono']
            id=request.POST['id']

            cliente=Clientes.objects.get(id=id)

            cliente.nombre = nom
            cliente.apellido =ape
            cliente.numeroTelefono=tel

            cliente.save()

            messages.success(request, 'Cliente agregado')

            return redirect('checho:listarClientes')

        else:
            
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarClientes')    

    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarClientes')

#datos de Empleado ----------------------------------->
def registrarEmpleado(request):
    admin=Administradores.objects.all()
    return render(request, 'empleado/registrarEmpleado.html',{'admin':admin})

def guardarEmpleado(request):
    
    try:
        if request.method == 'POST':
            nom=request.POST['nombre']
            apell=request.POST['apellido']
            numTel=request.POST['telefono']
            user=request.POST['user']
            contra=request.POST['passw']
            administrador=request.POST['admin']

            admin=Administradores.objects.get(id=administrador)
        
            q=Empleados.objects.create(nombre=nom,apellido=apell,numeroTelefono=numTel,usuario=user,contraseña=contra,administrador=admin)
            messages.success(request, 'Empleado agregado')
            return  redirect('checho:listarEmpleados')

        else:
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarEmpleados')    

    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarEmpleados')


def listarEmpleados(request):
    q=Empleados.objects.all()
    admin=Administradores.objects.all()
    pag = Paginator(q, 4)   #cinco registros por página
    page_number = request.GET.get('page')
        
        #sobreescribo el query
    q = pag.get_page(page_number)
        
    contexto = {'page_obj': q,'admin': admin}
    
    return render(request, 'empleado/listarEmpleados.html',contexto)    

def eliminarEmpleado(request, id):
    try:

        emple=Empleados.objects.get(id=id)

        emple.delete()
        messages.success(request, 'Empleado eliminado')
        return redirect('checho:listarEmpleados')

    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarEmpleados')


def editarEmpleado(request, id):


    emple=Empleados.objects.get(id=id)

    admin=Administradores.objects.all()

    return render(request, 'empleado/editarEmpleado.html', {'empleado': emple,'admin': admin})


def guardadoEmpleado(request):
    
    try:
        if request.method == 'POST':
            nom=request.POST['nombre']
            ape=request.POST['apellido']
            tel=request.POST['telefono']
            id=request.POST['id']
            admin=request.POST['admin']

            ad=Administradores.objects.get(id=admin)
            emple=Empleados.objects.get(id=id)

            emple.nombre=nom
            emple.apellido=ape
            emple.numeroTelefono=tel
            emple.administrador=ad

            emple.save()
            messages.success(request, 'Empleado Guardado')
            return  redirect('checho:listarEmpleados')
        else:
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarEmpleados')  
            
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarEmpleados')

def clientesBuscar (request):
    if request.method == "POST":
        
        from django.db.models import Q
        
        q = Clientes.objects.filter(
            Q(nombre__icontains = request.POST["dato"]) | 
            Q(apellido__icontains = request.POST["dato"]) 
           
        )
        
        pag = Paginator(q, 4)   #cinco registros por página
        page_number = request.GET.get('page')
        
        #sobreescribo el query
        q = pag.get_page(page_number)
        
        contexto = {'page_obj': q, "dato_buscado": request.POST["dato"]}

        return render(request,'usuario/listarClientesAjax.html',contexto)
    else:
        messages.warning(request, "Usted no envió datos...")
        return redirect('checho:listarClientes')



#datos del Administrador ------------------------------>
def registrarAdmin(request):
    return render(request, 'admin/registrarAdmin.html')    
def loginAdmin(request):
    return render(request, 'login/loginAdmin.html')   

def logearAdmin(request):
    try:
        if request.method == 'POST':
            user=request.POST['u']
            passw=request.POST['p']

            q = Administradores.objects.get(usuario = user, contraseña = passw)
            request.session["logueo"] = [q.id,q.usuario,q.rol]
            messages.success(request, 'Bienvenido')
            return  redirect('checho:index')
        else:
            messages.warning(request, "usuario o contraseña incorrectos ")
            return redirect('checho:loginAdmin')

    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:loginAdmin')  


def guardarAdmin(request):
    try:
        if request.method == 'POST':
            nom=request.POST['nombre']
            apell=request.POST['apellido']
            numTel=request.POST['telefono']
            user=request.POST['user']
            contra=request.POST['passw']

            q=Administradores.objects.create(nombre=nom,apellido=apell,numeroTelefono=numTel,usuario=user,contraseña=contra)

            messages.success(request, 'Administrador Guardado')
            
            return  redirect('checho:listarAdmin')
        else:
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarAdmin')

    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarAdmin')  

def listarAdmin(request):

    q=Administradores.objects.all()
    pag = Paginator(q, 4)   #cinco registros por página
    page_number = request.GET.get('page')
        
        #sobreescribo el query
    q = pag.get_page(page_number)
        
    contexto = {'page_obj': q}

    return render(request, 'admin/listarAdmin.html', contexto)    
def eliminarAdmin(request,id):    
    try:
        admin=Administradores.objects.get(id=id)

        admin.delete()
        messages.success(request, 'Administrador Eliminado')
        return redirect('checho:listarAdmin')
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarAdmin')  


def editarAdmin(request, id):

    admin=Administradores.objects.get(id=id)

    return render(request, 'admin/edicionAdmin.html', {'admin': admin})

def guardadoAdmin(request):

    try:
        if request.method == 'POST':

            nom=request.POST['nombre']
            ape=request.POST['apellido']
            tel=request.POST['telefono']
            id=request.POST['id']

            admin=Administradores.objects.get(id=id)

            admin.nombre = nom
            admin.apellido =ape
            admin.numeroTelefono=tel

            admin.save()
            messages.success(request, 'Administrador Guardado')
            return redirect('checho:listarAdmin')
        else:
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarAdmin')    

    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarAdmin') 




#Datos servicios------------------>


def registrarServicio(request):
    return render(request, 'servicios/registrarServicios.html')

def guardarServicio(request):
    try:
        if request.method == 'POST':
            nom=request.POST['nombre']
            price=request.POST['precio']
            q=Servicios.objects.create(nombreServicio=nom,precio=price) 

            messages.success(request, 'Servicio Guardado')

            return  redirect('checho:listarServicios')
        else:
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarServicios')
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarServicios')            

def listarServicios(request):
    q=Servicios.objects.all()
    pag = Paginator(q, 4)   #cinco registros por página
    page_number = request.GET.get('page')
        
        #sobreescribo el query
    q = pag.get_page(page_number)
        
    contexto = {'page_obj': q}
    return render(request, 'servicios/listarServicios.html', contexto)

def editarServicio(request,id):
    servi=Servicios.objects.get(id=id)
    return render(request, 'servicios/edicionServicio.html', {'servi': servi})

def guardarEdicionServicio(request):
    try:
        if request.method == 'POST':
            prec=request.POST['precio']    
            nomb=request.POST['nombre']   
            id=request.POST['id']   
            
            q=Servicios.objects.get(id=id)

            q.nombreServicio=nomb
            q.precio=prec
            q.save()
            messages.success(request, 'Servicio Guardado')
            return redirect( 'checho:listarServicios')

        else:
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarServicios')    
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarServicios')
        
def eliminarServicio(request,id):
    try:
        servi=Servicios.objects.get(id=id)
        servi.delete()
        messages.success(request, 'Servicio Eliminado')
        return redirect( 'checho:listarServicios')
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarServicios')

#Datos citas --------------------->


def agendarCita(request):

    empleados=Empleados.objects.all()
    servicios=Servicios.objects.all()
    

    contexto={

        'empleados': empleados,
        'servicios': servicios,
        
    }
    return render(request,'citas/agendarCita.html',contexto)

def guardarCita(request):
    
    try:
        login = request.session.get('logueo', False)
        if request.method == 'POST' and login:
            
            fech=request.POST['fecha']
            hor=request.POST['hora']
            emple=request.POST['empleados']
            servi=request.POST['servicios']
            cliente=Clientes.objects.get(id=login[0])
            empleado=Empleados.objects.get(id=emple)
            servicio=Servicios.objects.get(id=servi)

            cita=Citas.objects.create(fecha=fech, hora=hor, cliente=cliente, servicio=servicio,empleado=empleado)
            messages.success(request, 'Cita Agendada')
            return redirect('checho:listarCita')

        else:
            messages.warning(request, "Usted no envio datos ")
            return redirect('checho:listarCita')   

    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarCita')

def listarCita(request):

    q=Citas.objects.all()
    pag = Paginator(q, 4)   #cinco registros por página
    page_number = request.GET.get('page')
        
        #sobreescribo el query
    q = pag.get_page(page_number)
        
    contexto = {'page_obj': q}

    return render(request, 'citas/listarCita.html',contexto)


def eliminarCita(request,id):
    try:
        citas=Citas.objects.get(id=id)
        citas.delete()
        messages.success(request, 'Cita Agendada')
        return redirect('checho:listarCita')
    except Exception as e:
        messages.error(request, "Error: " + str(e))
        return redirect('checho:listarCita')
