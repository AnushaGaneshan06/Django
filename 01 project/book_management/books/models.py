from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)


# --------------def str ------------

# The __str__ method is a special method in Python. It controls how the object is represented as a string.

# -------Analogy--------
# Imagine you are meeting people at an event. Instead of saying, "Person object (1)", they introduce themselves with their name, like "Alice" or "Bob." The __str__ method is like teaching your model to introduce itself with a meaningful name. 
# 


# -------------------------

    def __str__(self):
        return "f{self.title} by {self.author}"
    


# --------step 2:---------

# Returning only the title is a design choice for simplicity.
# You can include more fields like author, publication_year, or genre if needed.