from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book

def index(request):
    """Displays all books for students and visitors."""
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def admin_signup(request):
    """Handles admin registration."""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.is_staff = True  # Mark user as admin
        user.save()
        messages.success(request, "Signup successful! You can now log in.")
        return redirect('login')
    
    return render(request, 'admin_signup.html')

from django.contrib.auth.models import User  # Import User model
from django.contrib import messages
from .models import AdminUser  # Import the correct model

def admin_login(request):
    """Handles admin login."""
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Fetch the user by email using the correct model
        try:
            user = AdminUser.objects.get(email=email)
        except AdminUser.DoesNotExist:
            messages.error(request, "No account found with this email.")
            return redirect('login')

        # Authenticate using the correct username field
        user = authenticate(request, username=user.username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password!")

    return render(request, 'admin_login.html')


@login_required
def dashboard(request):
    """Admin dashboard for managing books."""
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        published_date = request.POST['published_date']
        Book.objects.create(title=title, author=author, isbn=isbn, published_date=published_date)
        messages.success(request, "Book added successfully!")
        return redirect('dashboard')
    
    books = Book.objects.all()
    return render(request, 'dashboard.html', {'books': books})

@login_required
def update_book(request, book_id):
    """Allows admin to update a book record."""
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.published_date = request.POST['published_date']
        book.save()
        messages.success(request, "Book updated successfully!")
        return redirect('dashboard')

    return render(request, 'update_book.html', {'book': book})

@login_required
def delete_book(request, book_id):
    """Allows admin to delete a book record."""
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect('dashboard')

def logout_admin(request):
    """Logs out the admin."""
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
