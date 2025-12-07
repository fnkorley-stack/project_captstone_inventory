from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListCreateView.as_view()),
    path('<int:pk>/', views.ItemDetailView.as_view()),
    path('inventory-levels/', views.InventoryLevelView.as_view()),
]
