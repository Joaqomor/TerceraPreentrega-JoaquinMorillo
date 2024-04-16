from django.urls import path

from .views import (
    home_view,
    detail_view,
    list_view,
    search_view,
    search_with_form_view,
    create_with_form_view,
    create_client_with_form_view,
    detail_client_view,
    client_list_view,
    client_delete_view,
    client_update_view,
    search_client_view,
    office_list_view,
    create_office_with_form_view,
    detail_office_view,
    search_office_view,
    office_delete_view,
    delete_view,
    
    
)

urlpatterns = [
    path("", home_view),
    path("detail/<producto_id>", detail_view),
    path("list/", list_view, name="product-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-con-formulario/", search_with_form_view, name="zzz"),
    path("crear-producto-con-formulario/", create_with_form_view, name="product-create"),
    path("product/detail/<producto_id>", detail_view, name="product-detail"),
    path("product/delete/<producto_id>", delete_view, name="product-delete"),
    path("cliente/create/", create_client_with_form_view, name="client-create"),
    path("cliente/detail/<cliente_id>", detail_client_view, name="client-detail"),
    path("cliente/list/", client_list_view, name="client-list"),
    path("cliente/delete/<cliente_id>", client_delete_view, name="client-delete"),
    path("cliente/update/<cliente_id>", client_update_view, name="client-update"),
    path("cliente/buscar/", search_client_view, name="client-search"),
    path("sucursal/list/", office_list_view, name="office-list"),
    path("sucursal/create/", create_office_with_form_view, name="office-create"),
    path("sucursal/detail/<sucursal_id>", detail_office_view, name="office-detail"),
    path("sucursal/buscar/", search_office_view, name="office-search"),
    path("sucursal/delete/<sucursal_id>", office_delete_view, name="office-delete"),

]