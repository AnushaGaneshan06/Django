from django.contrib import admin
from django.urls import path
from display.views import display,functions,reverse_string, name, add_number,numbers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",display),
    path("functions/",functions),
    path("reverse/", reverse_string),
    path("name/", name),
    path("add/", add_number),
    path("numbers/", numbers)
]
