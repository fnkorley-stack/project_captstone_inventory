from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import InventoryItem
from .serializers import InventoryItemSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard pagination class for inventory items.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class ItemListCreateView(generics.ListCreateAPIView):
    """
    List all inventory items with pagination, filtering, searching, and ordering.
    Only authenticated users can create items.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['category', 'quantity']
    search_fields = ['name', 'category']
    ordering_fields = ['quantity', 'price', 'created_at']

    def perform_create(self, serializer):
        """
        Assign the logged-in user as the owner of the inventory item.
        """
        serializer.save(user=self.request.user)


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an inventory item.
    Only authenticated users can perform these actions.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """
        Ensure the logged-in user is assigned when updating.
        """
        serializer.save(user=self.request.user)


class InventoryLevelView(APIView):
    """
    View inventory levels for all items.
    Returns the item name, quantity, and stock status.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = InventoryItem.objects.all()
        data = [
            {
                "item": item.name,
                "quantity": item.quantity,
                "status": "LOW STOCK" if item.quantity < 5 else "OK"
            }
            for item in items
        ]
        return Response(data)
