from django.urls import path

from accounts.views.login_view import LoginView, logout_view
from accounts.views.profile_view import ProfileView
from accounts.views.register_view import RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout')
]