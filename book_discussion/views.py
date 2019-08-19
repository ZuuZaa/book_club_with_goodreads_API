from django.shortcuts import render, redirect
from books.models import Book
from .models import BookDiscussion
from django.contrib.auth.decorators import login_required

def discussion(request, id):
    book = Book.objects.get(id=id)
    discussions = BookDiscussion.objects.filter(book=id).order_by('-date')
    context = {
        'book': book,
        'discussions': discussions
    }

    if request.method == 'POST':
        if request.user.is_anonymous:
            return redirect('login')
        else:
            comment_text = request.POST.get('comment')
            new_comment = BookDiscussion(
                user = request.user,
                book = book,
                comment = comment_text
            )
            new_comment.save()
            return redirect('discussion', id)

    return render(request, 'discussion.html', context)