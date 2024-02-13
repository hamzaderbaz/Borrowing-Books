from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.authtoken.models import Token
from .models import Book, BorrowRecord
from .serializers import *
from .permissions import IsLibrarianOrReadOnly


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BorrowRecordListCreateView(generics.ListCreateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsLibrarianOrReadOnly]

    def perform_create(self, serializer):
        book_id = self.request.data.get('book')
        book = Book.objects.get(pk=book_id)

        if not book.available:
            raise serializers.ValidationError("This book is not available for borrowing.")

        user = self.request.user
        active_borrow_records = BorrowRecord.objects.filter(borrower=user, book=book, return_date=None)
        if active_borrow_records.exists():
            raise serializers.ValidationError("You cannot borrow the same book until you return it.")

        book.available = False
        book.save()
        serializer.save(borrower=user)

        return Response({'message': 'Book borrowed successfully.'}, status=status.HTTP_201_CREATED)


class BorrowRecordRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsLibrarianOrReadOnly]

    def perform_update(self, serializer):
        return_date = self.request.data.get('return_date')
        if return_date:
            book_id = serializer.instance.book.id
            book = Book.objects.get(pk=book_id)
            book.available = True
            book.save()
        serializer.save()

        return Response({'message': 'Book return processed successfully.'}, status=status.HTTP_200_OK)



class LoginView(APIView):
    
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
