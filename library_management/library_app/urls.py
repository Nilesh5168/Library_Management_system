from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import BookViewSet, register_admin, admin_login, logout_admin

router = DefaultRouter()
router.register(r'books', BookViewSet)  # CRUD for books

urlpatterns = [
    path('', include(router.urls)),  # Includes all endpoints for BookViewSet
    path('register/', register_admin, name='register_admin'),
    path('login/', admin_login, name='admin_login'),
    path('logout/', logout_admin, name='logout_admin'),

    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
