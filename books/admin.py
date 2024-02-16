from django.contrib import admin
from .models import Books

admin.site.site_header = 'Welcome to the library'
admin.site.index_title = 'My books'
admin.site.site_title = 'Library'

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'description')
    list_display = ('id', 'date_register', 'title', 'description', 'image')