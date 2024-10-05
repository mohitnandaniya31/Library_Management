from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def booksList(request):
    query = request.GET.get('QUERY')
    if query:
        books = BooksModel.objects.filter(title__icontains=query)
    else:
        books = BooksModel.objects.all()
    return render(request, 'books_list.html', {'books': books})

def booksDetail(request, book_id):
    book = get_object_or_404(BooksModel,  pk=book_id)
    return render(request, 'books_detail.html', {'book': book})
