from django.contrib import admin
from django.urls import path, include  # Include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library_app.urls')),  # Include the app's URLs
]
