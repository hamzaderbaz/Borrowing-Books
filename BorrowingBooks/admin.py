from django.contrib import admin
from .models import LibraryUser, Book, BorrowRecord


class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_owner')
    list_filter = ('is_owner',)
    search_fields = ('user__username',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'available')
    list_filter = ('available',)
    search_fields = ('title', 'author')


class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'borrower', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('book__title', 'borrower__username')


admin.site.register(LibraryUser, LibraryUserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)
