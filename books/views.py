from django.shortcuts import render, redirect
from .models import Books
from .forms import booksForm

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def books(request):
    books = Books.objects.all()
    return render(request, 'books/index.html', {'books': books})

def create(request):
    form = booksForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/create.html', {'form': form})

def update(request, id):
    id_book = Books.objects.get(id=id)
    form = booksForm(request.POST or None, request.FILES or None, instance=id_book)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('books')
    return render(request, 'books/update.html', {'form': form})

def delete(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect('books')