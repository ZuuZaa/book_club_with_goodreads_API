from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdate
from .models import Profile
from books.models import ReadenBook

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.info(request, f'{first_name} {last_name}, Kitab Klubumuza xoş gəldiniz, zəhmət olmasa sayta daxil olun.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def editprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, 
                               request.FILES, 
                               instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, f'{request.user.first_name} {request.user.last_name}, profiliniz yeniləndi.')
            return redirect('profile')
        else:
            messages.info(request, 'Bu kitabı artıq oxumusunuz.')
            return redirect('editprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'editprofile.html', context)

def profile(request):
    readen_books = ReadenBook.objects.filter(user = request.user)
    context = {
        'readen_books': readen_books
    }
    return render(request, 'profile.html', context)

def userprofile(request, user_id):
    profile = Profile.objects.get(user__id = user_id)
    readen_books = ReadenBook.objects.filter(user__id = user_id)
    context = {
        'profile': profile,
        'readen_books': readen_books,
    }
    return render(request, 'userprofile.html', context)