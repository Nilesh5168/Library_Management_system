📚 Library Management System

A web-based Library Management System built using Django with MySQL as the database. The system allows admins to manage books (add, update, delete) and students to view available books.

Overview
This is a Library Management System built using Django (Backend) and React (Frontend). It allows:
•	Students to view books.
•	Admins to add, update, and delete books.
•	Authentication for admin users.
________________________________________

🔧 Tech Stack
•	Backend: Django, Django REST Framework (DRF)
•	Frontend: React, React Router
•	Database: SQLite / PostgreSQL
•	Authentication: Token-based authentication
________________________________________

🚀 Setup Instructions

1️⃣ Backend Setup (Django)
📌 Install Dependencies
pip install -r requirements.txt

📌 Apply Migrations
python manage.py migrate

📌 Run Server
python manage.py runserver
Backend will run at http://127.0.0.1:8000/
________________________________________

2️⃣ Frontend Setup (React)
📌 Install Dependencies
npm install

📌 Start Development Server
npm start
Frontend will run at http://localhost:3000/
________________________________________

📚 API Endpoints

🔹 Authentication
✅ Register Admin
POST /api/register/
{
  "username": "admin1",
  "email": "admin@example.com",
  "password": "securepass"
}

✅ Admin Login
POST /api/login/
{
  "username": "admin1",
  "password": "securepass"
}

✅ Admin Logout
POST /api/logout/
________________________________________
🔹 Books Management

📌 Get All Books (No Authentication Required)
GET /api/books/

📌 Add Book (Admin Only)
POST /api/books/
{
  "title": "Book Title",
  "author": "Author Name",
  "isbn": "123456789",
  "published_date": "2025-03-19"
}

📌 Update Book (Admin Only)
PUT /api/books/{book_id}/
{
  "title": "Updated Title",
  "author": "Updated Author"
}

📌 Delete Book (Admin Only)
DELETE /api/books/{book_id}/
________________________________________

🎨 Frontend Features
📌 Navbar
•	Displays Student View for students.
•	Changes to Admin View after admin login.

📌 Home Page
•	Displays the list of books (accessible to everyone).

📌 Dashboard (Admin Only)
•	Allows admins to add, update, and delete books.
•	Automatically refreshes the book list after modifications.
________________________________________

🔥 Future Improvements

•	✅ Add user roles & permissions.
•	✅ Improve UI/UX with better styling.
•	✅ Implement JWT authentication.
________________________________________

🛠 Maintainers
•	Developer: Nilesh Patil
•	Contact: nileshpatil5168@gmail.com

Happy Coding! 🚀📚

