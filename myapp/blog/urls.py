from django.urls import path
from .import views

# importing views, name to identify
# module urls  tha path function
urlpatterns = [
    path('', views.index, name='form'),
    path('post/details', views.details, name="details"),

    # enter the number in server /view/6
    path("view/<int:post_id>", views.dynamic, name="dynamic"), # str give


    # ----------redirect-------
    path("new_url/", views.new_url_view, name="new_url"),

    path("old_url/", views.old_url_redirect, name="old_url"),

] 


