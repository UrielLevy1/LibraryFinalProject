from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    
    class BookType(models.IntegerChoices):
        ten_days = 1, "Ten Days Loan"
        five_days = 2, "Five Days Loan"
        two_days = 3, "Two Days Loan"
        
    name=models.CharField(max_length=50, null=False)
    author=models.CharField(max_length=50, null=False)
    year_published = models.DateField()
    type = models.SmallIntegerField(null=False, default = BookType.two_days, choices=BookType.choices)
    created_time=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    
    def __str__(self):
        return self.name
    
    
class Loan(models.Model):
    custID=models.ForeignKey(User, on_delete=models.CASCADE,)
    bookID=models.ForeignKey(Book, on_delete=models.CASCADE,)
    loan_date=models.DateTimeField()
    return_date=models.DateTimeField(null=True)
    
    def __str__(self):
        return self.return_date
    
    
class Author(models.Model):
    name=models.CharField(max_length=50, null=False)
    age=models.IntegerField()
    nationality=models.CharField(max_length=50, null=False)
    bookID=models.ForeignKey(Book, on_delete=models.CASCADE,related_name="tags", related_query_name="tag", null=True)
    image = models.ImageField(null=True, blank=True, default='/placeholder.png')
    
    def __str__(self):
        return str(self.name)
    
class Reviews(models.Model):
    stars=models.IntegerField(null=True, blank=True)
    text=models.CharField(max_length=500, null=True, blank=True)
    custID=models.ForeignKey(User, on_delete=models.CASCADE,)
    bookID=models.ForeignKey(Book, on_delete=models.CASCADE,)
    
    def __str__(self):
        return str(self.bookID)
    
        
    
    
    
