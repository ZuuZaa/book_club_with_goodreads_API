from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class BookDiscussion(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    
    def __str__(self):
        return f'User: {self.user.first_name} | Book: {self.book.title} | Time: {self.date}'