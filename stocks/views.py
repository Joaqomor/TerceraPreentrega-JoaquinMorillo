from django.shortcuts import render, redirect

from .forms import ProductoCreateForm, ProductoSearchForm, ClientCreateForm, ClienteSearchForm, SucursalCreateForm , SucursalSearchForm
from .models import Producto, Cliente, Sucursal




def home_view(request):
    return render(request, "stocks/home.html")

#---------------------Funciones para productos---------------------

def create_product_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_form": ProductoCreateForm() }
        return render(request, "stocks/productos/form_create.html", contexto)
    elif request.method == "POST":
        form = ProductoCreateForm(request.POST)
        if form.is_valid():
            nombre_de_producto = form.cleaned_data['nombre_de_producto']
            categoria = form.cleaned_data['categoria']
            precio = form.cleaned_data['precio']
            codigo = form.cleaned_data['codigo']
            descripcion = form.cleaned_data['descripcion']
            nuevo_producto = Producto(nombre_de_producto=nombre_de_producto, categoria=categoria, precio=precio,codigo=codigo, descripcion=descripcion)
            nuevo_producto.save()
            return detail_product_view(request, nuevo_producto.id)


def list_product_view(request):
    productos = Producto.objects.all()
    contexto_dict = {'todos_los_productos': productos}
    return render(request, "stocks/productos/list.html", contexto_dict)


def search_product_view(request, nombre_de_producto):
    todos_los_productos = Producto.objects.filter(nombre_de_producto=nombre_de_producto).all()
    contexto_dict = {"productos": todos_los_productos}
    return render(request, "stocks/productos/list.html", contexto_dict)


def search_product_with_form_view(request):
    if request.method == "GET":
        form = ProductoSearchForm()
        return render(request, "stocks/productos/form_search.html", context={"search_form": form})
    elif request.method == "POST":
        form = ProductoSearchForm(request.POST)
        if form.is_valid():
            nombre_de_producto = form.cleaned_data['nombre_de_producto']
        productos = Producto.objects.filter(nombre_de_producto=nombre_de_producto).all()
        contexto_dict = {"todos_los_productos": productos}
        return render(request, "stocks/list.html", contexto_dict)

def delete_product_view(request, producto_id):
    producto_a_borrar = Producto.objects.filter(id=producto_id).first()
    producto_a_borrar.delete()
    return redirect("product-list") 


def detail_product_view(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    contexto_dict = {"producto": producto}
    return render(request, "stocks/productos/detail.html", contexto_dict)

def update_product_view(request, producto_id):
    producto_a_editar = Producto.objects.filter(id=producto_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre_de_producto": producto_a_editar.nombre_de_producto,
            "categoria": producto_a_editar.categoria,
            "precio": producto_a_editar.precio,
            "codigo": producto_a_editar.codigo,
            "descripcion": producto_a_editar.descripcion
        }
        formulario = ProductoCreateForm(initial=valores_iniciales)
        contexto = {
            "form_update": formulario,
            "OBJETO": producto_a_editar
        }
        return render(request, "stocks/productos/form_update.html", contexto)
    elif request.method == "POST":
        form = ProductoCreateForm(request.POST)
        if form.is_valid():
            nombre_de_producto = form.cleaned_data['nombre_de_producto']
            categoria = form.cleaned_data['categoria']
            precio = form.cleaned_data['precio']
            codigo = form.cleaned_data['codigo']
            descripcion = form.cleaned_data['descripcion']
            producto_a_editar.nombre_de_producto = nombre_de_producto
            producto_a_editar.categoria = categoria
            producto_a_editar.precio = precio
            producto_a_editar.codigo = codigo
            producto_a_editar.descripcion = descripcion
            producto_a_editar.save()
            return redirect("product-detail", producto_a_editar.id)


#---------------------Funciones para clientes---------------------

def create_client_with_form_view(request):
    if request.method == "GET":
        contexto = {"client_form": ClientCreateForm()}
        return render(request, "stocks/clientes/form_create.html", contexto)
    elif request.method == "POST":
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            localidad = form.cleaned_data['localidad']
            nuevo_cliente = Cliente(nombre=nombre, telefono=telefono, email=email, localidad=localidad)
            nuevo_cliente.save()
            return detail_client_view(request, nuevo_cliente.id)



def detail_client_view(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    contexto_dict = {"cliente": cliente}
    return render(request, "stocks/clientes/detail.html", contexto_dict)


def client_list_view(request):
    clientes = Cliente.objects.all()
    contexto = {"todos_los_clientes": clientes}
    return render(request, "stocks/clientes/list.html", contexto)


def client_delete_view(request, cliente_id):
    cliente_a_borrar = Cliente.objects.filter(id=cliente_id).first()
    cliente_a_borrar.delete()
    return redirect("client-list")


def client_update_view(request, cliente_id):
    cliente_a_editar = Cliente.objects.filter(id=cliente_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": cliente_a_editar.nombre,
            "telefono": cliente_a_editar.telefono,
            "email": cliente_a_editar.email,
            "localidad": cliente_a_editar.localidad
        }
        formulario = ClientCreateForm(initial=valores_iniciales)
        contexto = {
            "form_update": formulario,
            "OBJETO": cliente_a_editar
        }
        return render(request, "stocks/clientes/form_update.html", contexto)
    elif request.method == "POST":
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            localidad = form.cleaned_data['localidad']
            cliente_a_editar.nombre = nombre
            cliente_a_editar.telefono = telefono
            cliente_a_editar.email = email
            cliente_a_editar.localidad = localidad
            cliente_a_editar.save()
            return redirect("client-detail", cliente_a_editar.id)


def search_client_view(request):
    if request.method == "GET":
        form = ClienteSearchForm()
        return render(request, "stocks/clientes/form_search.html", context={"search_form": form})
    elif request.method == "POST":
        form = ClienteSearchForm(request.POST)
        if form.is_valid():
            localidad = form.cleaned_data['localidad']
        clientes = Cliente.objects.filter(localidad=localidad).all()
        contexto_dict = {"todos_los_clientes": clientes}
        return render(request, "stocks/clientes/list.html", contexto_dict)
    
    
#---------------------Funciones para sucursales---------------------

def office_list_view(request):
    sucursales = Sucursal.objects.all()
    contexto = {"todas_las_sucursales": sucursales}
    return render(request, "stocks/sucursales/list.html", contexto)

def create_office_with_form_view(request):
    if request.method == "GET":
        contexto = {"office_form": SucursalCreateForm()}
        return render(request, "stocks/sucursales/form_create.html", contexto)
    elif request.method == "POST":
        form = SucursalCreateForm(request.POST)
        if form.is_valid():
            tipo_de_sucursal = form.cleaned_data['tipo_de_sucursal']
            tamaño = form.cleaned_data['tamaño']
            localidad = form.cleaned_data['localidad']
            cantidad_de_empleados = form.cleaned_data['cantidad_de_empleados']
            nueva_sucursal = Sucursal(tipo_de_sucursal=tipo_de_sucursal, tamaño=tamaño, localidad=localidad, cantidad_de_empleados=cantidad_de_empleados)
            nueva_sucursal.save()
            return detail_office_view(request, nueva_sucursal.id)
        
def detail_office_view(request, sucursal_id):
    sucursal = Sucursal.objects.get(id=sucursal_id)
    contexto_dict = {"sucursal": sucursal}
    return render(request, "stocks/sucursales/detail.html", contexto_dict)

def search_office_view(request):
    if request.method == "GET":
        form = SucursalSearchForm()
        return render(request, "stocks/sucursales/form_search.html", context={"search_form": form})
    elif request.method == "POST":
        form = SucursalSearchForm(request.POST)
        if form.is_valid():
            tipo_de_sucursal = form.cleaned_data['tipo_de_sucursal']
        sucursales = Sucursal.objects.filter(tipo_de_sucursal=tipo_de_sucursal).all()
        contexto_dict = {"todas_las_sucursales": sucursales}
        return render(request, "stocks/sucursales/list.html", contexto_dict)
    
   
def office_delete_view(request, sucursal_id):
    sucursal_a_borrar = Sucursal.objects.filter(id=sucursal_id).first()
    sucursal_a_borrar.delete()
    return redirect("office-list")   

def office_update_view(request, sucursal_id):
    sucursal_a_editar = Sucursal.objects.filter(id=sucursal_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "tipo_de_sucursal": sucursal_a_editar.tipo_de_sucursal,
            "tamaño": sucursal_a_editar.tamaño,
            "localidad": sucursal_a_editar.localidad,
            "cantidad_de_empleados": sucursal_a_editar.cantidad_de_empleados
        }
        formulario = SucursalCreateForm(initial=valores_iniciales)
        contexto = {
            "form_update": formulario,
            "OBJETO": sucursal_a_editar
        }
        return render(request, "stocks/sucursales/form_update.html", contexto)
    elif request.method == "POST":
        form = SucursalCreateForm(request.POST)
        if form.is_valid():
            tipo_de_sucursal = form.cleaned_data['tipo_de_sucursal']
            tamaño = form.cleaned_data['tamaño']
            localidad = form.cleaned_data['localidad']
            cantidad_de_empleados = form.cleaned_data['cantidad_de_empleados']
            sucursal_a_editar.tipo_de_sucursal = tipo_de_sucursal
            sucursal_a_editar.tamaño = tamaño
            sucursal_a_editar.localidad = localidad
            sucursal_a_editar.cantidad_de_empleados = cantidad_de_empleados
            sucursal_a_editar.save()
            return redirect("office-detail", sucursal_a_editar.id)