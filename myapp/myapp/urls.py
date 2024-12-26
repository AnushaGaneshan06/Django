from django.contrib import admin
from django.urls import path,include 


urlpatterns = [
    path('blog/', include('blog.urls')),
    path("admin/", admin.site.urls),

]

# -------------404-----------
# importing the include function to import blog urls here
# variable assign 404

from myapp.views import custom_page_not_found

handler404 = "myapp.views.custom_page_not_found"
# ---------------------
