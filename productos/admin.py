from django.contrib import admin
from productos.models import (
    Producto, ProdcutoImagen, LogBuy
)


class ProductoImagenInLine(admin.TabularInline):
    model = ProdcutoImagen


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductoImagenInLine
    ]


admin.site.register(Producto, ProductAdmin)
admin.site.register(LogBuy)
