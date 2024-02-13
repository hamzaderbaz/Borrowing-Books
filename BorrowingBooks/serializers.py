from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class LibraryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = '__all__'

    def validate(self, data):
        if data.get('is_owner', False):
            user = data.get('user')
            if BorrowRecord.objects.filter(borrower=user, return_date__isnull=True).exists():
                raise serializers.ValidationError("User is already a borrower and cannot be marked as an owner.")
        return data


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
   
    
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    is_owner = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'is_owner']

    def validate(self, data):
        password1 = data.get('password')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        
        user.set_password(password)
        user.save()
        
        LibraryUser.objects.create(user=user, is_owner=self.validated_data['is_owner'])
        return user