from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from django.conf.urls import include
from django.conf.urls.static import static
from books import views
from books import my_login

app_name = "books"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('books.urls')),
    path('login/', my_login.login_page, name="login"),
    path('register/', my_login.registration, name="register"),
    # path('books',include('books.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)