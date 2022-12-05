from django.shortcuts import render, redirect
from django.http import HttpResponse
from books.forms import BookForm, AuthorForm, LoanForm, ReviewForm
from books.models import Book, Author, Loan, Reviews
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate


def home(request):
    return render(request,'books/home.html')


@login_required 
def books_list(request):
    my_books = Book.objects.all()
    context = {
        'book_list': my_books,
    }
    return render(request,'books/books.html', context=context)

@login_required 
def loans_list(request):
    all_loans = Loan.objects.all()
    context = {
        'loans_list': all_loans,
    }
    return render(request,'books/all_loans.html', context=context)

@login_required 
def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request,'books/authors.html', context=context)

@login_required 
def add_author(request):
    context = {
        'authorform' : AuthorForm(),
    }
    return render(request, 'books/add_author.html', context)

def add_author_action(request):
    authorform = AuthorForm(request.POST, request.FILES)
    if authorform.is_valid():
        authorform.save()
        return redirect('books:authors')
    else:
        print("error")
        context = {
            'authorform': AuthorForm,
        }
        return render(request, 'add_author.html', context)
    
    
def loan_book(request):
    context = {
        'loanform' : LoanForm(),
    } 
    return render(request, 'books/loan_book.html', context)   

def loan_book_action(request):
    loanform = LoanForm(request.POST, request.FILES)
    if loanform.is_valid():
        loanform.save()
        return redirect('books:books_list')
    else:
        print("error")
        context = {
            'loanform' : loanform,
        }
        return render(request, 'books/loan_book.html', context)


def add_book(request):
    context = {
        'bookform' : BookForm(), 
    }
    return render(request,'books/add_book.html', context)

def add_book_action(request):
    bookform = BookForm(request.POST, request.FILES)
    if bookform.is_valid():
        bookform.save()
        return redirect('books:books_list')
    else:
        print("error")
        context = {
            'bookform': bookform,
        }
        return render(request, 'addbook.html', context)


@login_required
def search(request):
    my_search = request.GET.get('search')
    my_books = Book.objects.filter(name__contains=my_search)
    context = {
            'book_list': my_books,
    }   
    return render(request, 'books/books.html', context=context)

@login_required
def search_by_author(request):
    my_search = request.GET.get('search')
    my_books = Book.objects.filter(author__contains=my_search)
    context = {
            'book_list': my_books,
    }   
    return render(request, 'books/books.html', context=context)

def delete(request, pk):
    Book.objects.filter(id=pk).delete()
    # user = authenticate(request)
    # if user is None:
    messages.error(request, "Book deleted")
    return redirect('books:books_list')


def delete_author(request, pk):
    Author.objects.filter(id=pk).delete()
    messages.error(request, "Author deleted")
    return redirect('books:authors')


def addreview(request):
    context = {
        'reviewform' : ReviewForm(), 
    }
    return render(request,'books/add_review.html', context)
    
def add_review_action(request):
    reviewform = ReviewForm(request.POST, request.FILES)
    if reviewform.is_valid():
        reviewform.save()
        return redirect('books:reviews_list')
    else:
        print("error")
        context = {
            'reviewform': reviewform,
        }
        return render(request, 'addreview.html' , context)    
    
    
@login_required 
def reviews_list(request):
    all_reviews = Reviews.objects.all()
    context = {
        'reviews_list': all_reviews,
    }
    return render(request,'books/reviews.html', context=context)    