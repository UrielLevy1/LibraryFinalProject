from django.forms import ModelForm
from .models import Book, Author, Loan, Reviews
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'        

class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'       
        
class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'  
        
        
class CreateuserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        
        
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'year_published', 'type', 'image']        
        
        