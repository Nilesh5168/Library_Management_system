📚 Library Management System

A web-based Library Management System built using Django with MySQL as the database. The system allows admins to manage books (add, update, delete) and students to view available books.

Features:
•	Admin Authentication (Login/Logout)
•	Admin Dashboard (Manage Books)
•	Book Management (CRUD operations)
•	Student View (View available books)
•	MySQL Database Integration
•	Responsive UI


Setup Instructions:

1)Install Dependencies
•	pip install django mysqlclient

2) Configure MySQL Database
  1.	Open MySQL Workbench or any MySQL client.
  2.	Create a new database:     CREATE DATABASE library_db;
     
3) Apply Migrations(Run following commands)
•	python manage.py makemigrations
•	python manage.py migrate

4) Create Superuser (Admin)
•	python manage.py createsuperuser

5) Run the Server
•	python manage.py runserver



📁 Project Structure

library_management/
│── library_app/         # Django App (Models, Views, Templates)
│   ├── migrations/      # Database Migrations
│   ├── templates/       # HTML Templates
│   ├── static/          # CSS & JS files
│   ├── views.py         # Business Logic
│   ├── models.py        # Database Models
│   ├── urls.py          # URL Routing
│── library_management/  # Main Project Folder
│   ├── settings.py      # Django Settings
│   ├── urls.py          # Project URL Configuration
│── manage.py            # Django CLI
│── README.md            # Project Documentation

✅ Assumptions

Admins manage books (CRUD operations).
Students can only view books.
User authentication is required for admin access.


Future Improvements:

Add student authentication & borrowing system.
Implement book search and filters.
Improve UI/UX with Bootstrap or TailwindCSS.


License:

This project is open-source under the MIT License.


