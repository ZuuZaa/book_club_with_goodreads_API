from django.shortcuts import render
from books.models import *

def home(request):
    current_books = CurrentBook.objects.all()
    book_in_vote = BookInVote.objects.order_by('-vote')[:5]
    context = {
        'current_books': current_books,
        'book_in_vote': book_in_vote
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {'title':'Haqqimizda'})


     