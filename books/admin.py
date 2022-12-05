from django.contrib import admin

# Register your models here.

from .models import Book, Loan, Author, Reviews

admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Author)
admin.site.register(Reviews)

