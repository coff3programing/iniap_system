from django.urls import path
from .views import *

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('books/', books, name='books'),
    path('books/create/', create, name='create'),
    path('books/update', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('books/update/<int:id>', update, name='update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
