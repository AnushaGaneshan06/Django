from django.contrib import admin
from django.urls import path,include 
# importing the include function to import blog urls here

urlpatterns = [
    path('blog/', include('blog.urls')),
    path("admin/", admin.site.urls),
]
