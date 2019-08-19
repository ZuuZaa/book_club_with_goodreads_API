from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
   title = models.CharField(max_length = 250)
   author = models.CharField(max_length = 250)
   image = models.ImageField(upload_to='booker/book_covers', null = True, blank = True)
   small_image = models.ImageField(upload_to='booker/small_book_covers', null = True, blank = True)
   year = models.IntegerField(null = True, blank = True)
   vote = models.IntegerField(default = 0)
   good_id = models.IntegerField(default = 1)
   discussed = models.BooleanField(default=False)

   def __str__(self):
      return f'{self.title} | by {self.author}' 


class BookInVote(models.Model):
   book_in_vote = models.OneToOneField(Book, on_delete = models.CASCADE)
   vote = models.IntegerField(default = 0)

   def __str__(self):
      return f'{self.book_in_vote.title} | by {self.book_in_vote.author}' 


class CurrentBook(models.Model):
   current_book = models.OneToOneField(Book, on_delete = models.CASCADE)

   def __str__(self):
      return f'{self.current_book.title} | by {self.current_book.author}' 


class VotedBook(models.Model):
   voted_book = models.ForeignKey(Book, on_delete = models.CASCADE, null = True, blank = True)
   user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

   def __str__(self):
      return f'{self.voted_book.title} | voted by {self.user.first_name} {self.user.last_name}' 


class ReadenBook(models.Model):
   readen_book = models.ForeignKey(Book, on_delete = models.CASCADE, null = True, blank = True)
   user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

   def __str__(self):
      return f'{self.readen_book.title} | readen by {self.user.first_name} {self.user.last_name}' 
   