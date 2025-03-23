from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth import authenticate, login
from .models import Book, AdminUser
from .serializers import BookSerializer

# Register Admin User
@api_view(['POST'])
@permission_classes([AllowAny])
def register_admin(request):
    """Registers an admin user."""
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if AdminUser.objects.filter(email=email).exists():
        return Response({"error": "Email already in use!"}, status=status.HTTP_400_BAD_REQUEST)

    user = AdminUser.objects.create_user(username=username, email=email, password=password, is_staff=True)
    return Response({"message": "Admin registered successfully!"}, status=status.HTTP_201_CREATED)

# Admin Login
@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
    """Handles admin login."""
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid username or password!"}, status=status.HTTP_401_UNAUTHORIZED)

# Logout Admin
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_admin(request):
    """Logs out the admin user."""
    return Response({"message": "Logged out successfully!"}, status=status.HTTP_200_OK)

# Books Viewset for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can read, only authenticated users can modify

# List all books (No authentication required)
@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    """Displays all books for everyone (including unauthenticated users)."""
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Add a new book (Only Admins)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_book(request):
    """Adds a new book."""
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update a book (Only Admins)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_book(request, book_id):
    """Updates a book."""
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a book (Only Admins)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_book(request, book_id):
    """Deletes a book."""
    try:
        book = Book.objects.get(pk=book_id)
        book.delete()
        return Response({"message": "Book deleted successfully!"}, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
