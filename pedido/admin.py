from django.contrib import admin
from . import models

class ItemPeidoInLine(admin.TabularInline):
    model = models.ItemPedido
    extra = 1
    
class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPeidoInLine
    ]

admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)


