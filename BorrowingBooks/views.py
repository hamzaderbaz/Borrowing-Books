from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny  
from .models import *
from .serializers import *
from .permissions import *


class LibraryUserListCreateView(generics.ListCreateAPIView):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user

        library_user = user.libraryuser
        if not library_user.is_owner:
            raise serializers.ValidationError("Only owners can add books.")
        return super().perform_create(serializer)


class BorrowRecordListCreateView(generics.ListCreateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        book_id = self.request.data.get('book')
        book = Book.objects.get(pk=book_id)

        if not book.available:
            raise serializers.ValidationError("This book is not available for borrowing.")

        user = self.request.user
        active_borrow_records = BorrowRecord.objects.filter(borrower=user, book=book, return_date=None)
        if active_borrow_records.exists():
            raise serializers.ValidationError("You cannot borrow the same book until you return it.")

        library_user = user.libraryuser
        if library_user.is_owner:
            raise serializers.ValidationError("owners cannot borrow books.")

        book.available = False
        book.save()
        serializer.save(borrower=user)
        return Response({'message': 'Book borrowed successfully.'}, status=status.HTTP_201_CREATED)


class BorrowRecordRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsOwnerOrReadOnly]

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
        token = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

  
class UserRegistrationAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)