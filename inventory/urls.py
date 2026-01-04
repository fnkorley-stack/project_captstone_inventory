from django.urls import path
from .views import (
    ItemListCreateView,
    ItemDetailView,
    InventoryLevelView
)

urlpatterns = [
    path("items/", ItemListCreateView.as_view(), name="inventory-list-create"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="inventory-detail"),
    path("levels/", InventoryLevelView.as_view(), name="inventory-levels"),
]
