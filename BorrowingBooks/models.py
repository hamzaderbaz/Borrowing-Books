from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LibraryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    def set_available(self, status=True):
        self.available = status
        self.save()


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Borrow Record: {self.book} - Borrower: {self.borrower}"

    def clean(self):
        if not self.book.available:
            raise ValidationError("The book is not available for borrowing.")

    def save(self, *args, **kwargs):
        self.full_clean()  
        self.book.set_available(False) 
        super().save(*args, **kwargs)
