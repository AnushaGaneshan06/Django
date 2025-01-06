from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name= "book_list"),
    path('add/', views.book_add, name = "book_add"),
    path("edit/<int:book_id>/", views.book_edit, name = "book_edit"),
    path('delete/<int:book_id>/', views.book_delete, name='delete_book'),

]
