from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def book_list(request): 
    books = Book.objects.all()
    # etrieves all the books from the database.
    return render(request, 'books/book_list.html', {"books": books})

# --------------add the books------------

# f the method is POST, the data from the form (title, author, publication_year, genre) is retrieved using request.POST.

def book_add(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        publication_year = request.POST["publication_year"]
        genre = request.POST["genre"]
        Book.objects.create(title = title, author = author, publication_year = publication_year, genre = genre)
# After saving the new book, redirect('book_list')
        return redirect("book_list")
    
    return render (request, 'books/book_add.html')


# --------------------edit the books--------

def book_edit(request, book_id):
    book = get_object_or_404(Book, id= book_id)
    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.publication_year = request.POST["publication_year"]
        book.genre = request.POST["genre"]
        book.save()
        return redirect("book_list")
    return render(request, "books/book_edit.html", {'book' : book})

# ---delete book---------

def book_delete(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    book.delete()
    return redirect("book_list")


