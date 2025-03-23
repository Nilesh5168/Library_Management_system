# from rest_framework import serializers
# from .models import AdminUser, Book

# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdminUser
#         fields = ['id', 'username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = AdminUser.objects.create_user(**validated_data)
#         return user

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
