from django.db import models
from django.contrib.auth.models import User
from books.models import *

# Create your models here.
class BorrowModel(models.Model):
    BOOK_STATUS = [
    ('BORROW', 'BORROW'),
    ('REQUEST', 'REQUEST'),
    ('CANCEL', 'CANCEL'),
    ('RETURN', 'RETURN'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
    request_at = models.DateTimeField(auto_now_add=True)
    borrow_at = models.DateTimeField(null=False, blank=False)
    update_at= models.DateTimeField(auto_now=True)
    return_at = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=7, choices=BOOK_STATUS, default='REQUEST')
    def __str__(self):
        return f'status : {self.status.lower()}, {self.book} borrowed by {self.user.username}'