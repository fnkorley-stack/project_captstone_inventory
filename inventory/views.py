from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import InventoryItem
from .serializers import InventoryItemSerializer


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['category', 'quantity']
    search_fields = ['name', 'category']
    ordering_fields = ['quantity', 'created_at']


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]


class InventoryLevelView(APIView):
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
