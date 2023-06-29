from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", store, name="store"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
]