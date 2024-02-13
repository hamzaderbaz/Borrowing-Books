from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from dj_rest_auth.views import LoginView, LogoutView
from BorrowingBooks.views import UserRegistrationAPIView

schema_view = get_schema_view(
    
    openapi.Info(
        title='BorrowingBooks',
        default_version='v1',
        description="BorrowingBooks API",
        terms_of_service="https://www.BorrowingBooks.com/terms/",
        contact=openapi.Contact(email="contact@BorrowingBooks.com"),
        license=openapi.License(name="BorrowingBooks License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BorrowingBooks.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 


    # API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/login/', LoginView.as_view(), name='rest_login'),
    path('api/auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/auth/registration/', UserRegistrationAPIView.as_view(), name='rest_logout'),

]