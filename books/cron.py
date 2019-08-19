from books.models import BookInVote, CurrentBook, VotedBook
from django.shortcuts import render


def replace(request):
    CurrentBook.objects.all().delete()

    new_books = BookInVote.objects.order_by('-vote')[:5]

    for book in new_books:
        current_book = CurrentBook(current_book = book.book_in_vote)
        current_book.save()
    
    BookInVote.objects.all().delete()
    VotedBook.objects.all().delete()

    return render(request, 'book.html')


