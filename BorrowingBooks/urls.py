from django.urls import path
from .views import *
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('library-users/', LibraryUserListCreateView.as_view(), name='library-user-list-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('borrow-records/', BorrowRecordListCreateView.as_view(), name='borrow-record-list-create'),
    path('borrow-records/<int:pk>/', BorrowRecordRetrieveUpdateView.as_view(), name='borrow-record-retrieve-update'),
    path('login/', LoginView.as_view(), name='login'),
    path('docs/', include_docs_urls(title='Library Management API', public=True)),
]





# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import LibraryUserViewSet, BookViewSet, BorrowRecordViewSet

# router = DefaultRouter()
# router.register(r'library-users', LibraryUserViewSet, basename='libraryuser')
# router.register(r'books', BookViewSet, basename='book')
# router.register(r'borrow-records', BorrowRecordViewSet, basename='borrowrecord')

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]
