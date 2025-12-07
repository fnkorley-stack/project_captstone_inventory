from django.urls import path
from .views import UserListCreateView, UserDetailView, LoginView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('login/', LoginView.as_view()),  # Login
]
