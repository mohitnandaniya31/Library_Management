from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BooksModel(models.Model):
    BOOK_CATEGORY = [
    ('SCIENCE', 'SCIENCE'),
    ('SOCIAL', 'SOCIAL'),
    ('BIOGRAPHY', 'BIOGRAPHY'),
    ('HORROR', 'HORROR'),
    ('ACTION', 'ACTION'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=12, choices=BOOK_CATEGORY, default='CLASSICS')
    author = models.CharField(max_length=100, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    price = models.FloatField(null=False, blank=False, default=01.00)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    write_at = models.IntegerField(null=False, blank=False)
    # stock = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.title} book written by {self.author}'