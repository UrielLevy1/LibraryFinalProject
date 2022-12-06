from django.urls import path
from . import views

app_name = "books"

urlpatterns = [

path('',views.home, name="home"),
path('home',views.home, name="home"),
path('bookslist', views.books_list, name="books_list"),
path('loanslist', views.loans_list, name="loans_list"),
path('addbook',views.add_book, name="addbook"),
path('add_book_action/', views.add_book_action, name="add_book_action"),
path('search/', views.search, name="search"),
path('search_by_author/', views.search_by_author, name="search2"),
path('delete/<pk>/', views.delete, name="delete"),
path('authors/', views.authors, name="authors"),
path('delete_author/<pk>/', views.delete_author, name="delete_author"),
path('addauthor/', views.add_author, name="addauthor"),
path('add_author_action/', views.add_author_action, name="add_author_action"),
path('loanbook/', views.loan_book, name="loanbook"),
path('loan_book_action/', views.loan_book_action, name="loan_book_action"),
path('addreview/', views.addreview, name="addreview"),
path('add_review_action', views.add_review_action, name="add_review_action"),
path('reviews', views.reviews_list, name="reviews"),
]