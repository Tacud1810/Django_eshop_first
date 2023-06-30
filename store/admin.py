from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


# Register your models here.
class OrderItemInLine(admin.TabularInline):
	model = OrderItem
	extra = 0


class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'date_ordered', 'customer')
	inlines = [OrderItemInLine]


admin.site.register(Customer)
admin.site.register(Product)
# admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Order, OrderAdmin)
