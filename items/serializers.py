from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'stock_quantity', 'item_price']
