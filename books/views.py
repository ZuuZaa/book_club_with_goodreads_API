from django.shortcuts import render, redirect
from .models import Book, BookInVote, VotedBook, ReadenBook
from django.contrib import messages
from .goodreads import get_book_list, get_specific_book
from django.contrib.auth.decorators import login_required

def vote_page(request):
    context = {
        'books_in_vote': BookInVote.objects.all().order_by('-vote')
    }
    return render(request, 'book.html', context)
    

def search(request):
   if request.method == 'POST':
       name = request.POST.get('book_name')
       books_from_api = get_book_list(name)
       if len(books_from_api):
           context = {
               'books_from_api': get_book_list(name),
               'search_title': name
           }
           return render(request, 'search.html', context)
       else:
           messages.info(request, 'Kitab tapilmadi.')
   return render(request, 'search.html')

        
def choose_book(request):
    if request.method == 'POST':  
        name, index = request.POST.get('index').split('-')
        book_info = get_specific_book(name, int(index))
        exist_in_archive = Book.objects.filter(good_id = book_info['good_id'])

        if len(exist_in_archive):
            exist_in_vote = BookInVote.objects.filter(book_in_vote = exist_in_archive[0])
            if len(exist_in_vote):
                messages.info(request, 'Seçdiyiniz kitab səsvermə siyahısında mövcuddur.')
            else:
                vote_book = BookInVote(book_in_vote = exist_in_archive[0])
                vote_book.save()
                messages.info(request, 'Seçdiyiniz kitab səsvermə üçün kitablar siyahısına daxil edildi.')
        else:   
            new_book = Book(
                title = book_info['title'],
                author = book_info['author'],
                year= book_info['year'],
                image = book_info['image'],
                small_image = book_info['small_image'],
                good_id = book_info['good_id']
            )
            new_book.save()
            vote_book = BookInVote(book_in_vote = new_book)
        
            vote_book.save()
            messages.info(request, 'Seçdiyiniz kitab səsvermə üçün kitablar siyahısına daxil edildi.')

        return redirect('vote_page')

@login_required    
def vote(request, b_id):
    if request.method == 'POST':
        book = Book.objects.get(pk=b_id)
        voted = VotedBook.objects.filter(voted_book=book, user=request.user)
        if len(voted):
            messages.info(request, 'Bu kitaba artıq səs vermisiniz.')
        else:
            book.vote +=1
            vote_book = BookInVote.objects.get(book_in_vote=book)
            vote_book.vote +=1
            just_voted = VotedBook(voted_book=book, user=request.user)
            book.save()
            vote_book.save()
            just_voted.save()
            messages.info(request, f'{book.title} üçün səsiniz qeydə alındı.')
    return redirect('vote_page')
    

def readen(request, id):
    book = Book.objects.get(id=id)
    check_list = ReadenBook.objects.filter(readen_book = book, user = request.user)
    if not len(check_list):
        readen_book = ReadenBook(readen_book = book, user = request.user)
        readen_book.save()
        messages.info(request, f'{book.title} oxuduğunuz kitablar siyahısına əlavə olundu.')
    else:
        messages.info(request, 'Bu kitabı artıq oxumusunuz.')
    return redirect('book-home')        

def archive(request):
    if request.method == 'POST':
        name = request.POST.get('book_name')
        books_in_vote = Book.objects.filter(discussed = True, title__icontains = name)
        if not len(books_in_vote):
            messages.info(request, 'Axtardiginiz kitap, muzakire olunmus kitablar arasinda yoxdur.')
    else:
        books_in_vote = Book.objects.filter(discussed = True)

    context = {
        'books_in_vote': books_in_vote
    }
    return render(request, 'archive.html', context)