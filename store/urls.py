from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	path("admin/", admin.site.urls),
	path("", store, name="store"),
	path("cart/", cart, name="cart"),
	path("checkout/", checkout, name="checkout"),

	path("update_item/", update_item, name="update_item"),
	path("proccess_order/", proccess_order, name="proccess_order"),

]
