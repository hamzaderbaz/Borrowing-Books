from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Borrow Record: {self.book} - Borrower: {self.borrower}"

    def save(self, *args, **kwargs):
        if not self.book.available:
            raise ValidationError("The book is not available for borrowing.")

        super().save(*args, **kwargs)
        return "BorrowRecord saved successfully."
