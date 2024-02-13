from django.contrib import admin
from .models import Book, BorrowRecord

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'available')
    list_filter = ('available',)
    search_fields = ('title', 'author')

class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'borrower', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('book__title', 'borrower__username')


admin.site.register(Book, BookAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)
