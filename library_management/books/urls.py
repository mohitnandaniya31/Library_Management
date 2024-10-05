from django.urls import path
from . import views

urlpatterns = [
    path('',  views.booksList, name='booksList'),
    path('<int:book_id>/',  views.booksDetail, name='booksDetail'),
]
