from django import forms

from .models import Producto, Cliente, Sucursal


class ProductoSearchForm(forms.Form):
    nombre_de_producto = forms.CharField(max_length=50, required=True, label="Ingresar nombre de un producto")
    
class ClienteSearchForm(forms.Form):
    localidad = forms.CharField(max_length=50, required=True, label="Ingresar Localidad")
    
class SucursalSearchForm(forms.Form):
    tipo_de_sucursal = forms.CharField(max_length=50, required=True, label="Ingresar tipo de sucursal")


class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email', 'localidad']
        labels = {
            'nombre': 'Nombre',
            'telefono': 'Telefono',
            'email': 'Email',
            'localidad': 'Localidad',
        }


class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_de_producto', 'categoria', 'precio', 'codigo', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),  
        }
        
class SucursalCreateForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['tipo_de_sucursal', 'tamaño', 'localidad', 'cantidad_de_empleados']
        

    
        