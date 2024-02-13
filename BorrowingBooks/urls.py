from django.urls import path
from .views import *
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('borrow-records/', BorrowRecordListCreateView.as_view(), name='borrow-record-list-create'),
    path('borrow-records/<int:pk>/', BorrowRecordRetrieveUpdateView.as_view(), name='borrow-record-retrieve-update'),
    path('login/', LoginView.as_view(), name='login'),
    path('docs/', include_docs_urls(title='Library Management API', public=True)),
]
