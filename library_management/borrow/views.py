from django.shortcuts import render
from .models import *

# Create your views here.
def borrowList(request):
    query = request.GET.get('QUERY')
    if query:
        borrowed_books = BorrowModel.objects.filter(status__icontains=query)
    else:
        borrowed_books =  BorrowModel.objects.all()
    return render(request,  'borrow_list.html', {'borrowed_books':borrowed_books})