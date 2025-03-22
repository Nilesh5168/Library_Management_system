from django.urls import path
from .views import index, admin_signup, admin_login, dashboard, update_book, delete_book, logout_admin

urlpatterns = [
    path('', index, name='index'),
    path('signup/', admin_signup, name='signup'),
    path('login/', admin_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('update_book/<int:book_id>/', update_book, name='update_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('logout/', logout_admin, name='logout'),
]
