from django.contrib import admin
from .models import Categoria, Insumo, Producto
# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    pass


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'stock')
    list_editable = ('stock',)
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    filter_horizontal = ('insumo',)