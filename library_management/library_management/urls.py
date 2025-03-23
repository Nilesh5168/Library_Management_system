from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('api/', include('library_app.urls')),  # API endpoints from app-level urls.py
]
