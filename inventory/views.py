from rest_framework import generics
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class InventoryLevelView(APIView):
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
