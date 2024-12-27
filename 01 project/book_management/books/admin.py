from django.contrib import admin
from .models import Book

admin.site.register(Book)

# ---------------explanation----------

# 1.  makes the Book model accessible through the Django Admin panel.
# 2.  This lets you easily manage the model's data without writing any additional code.
# 3. You can customize the way the model appears in the admin interface using options like list_display or even by creating custom admin classes.