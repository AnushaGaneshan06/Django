from django.urls import path
from .import views

urlpatterns = [
    path("", views.cal_view, name = "calc"),
]