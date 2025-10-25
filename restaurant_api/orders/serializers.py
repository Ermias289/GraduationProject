from rest_framework import serializers
from .models import Order, OrderItem
from menu.models import MenuItem
from menu.serializers import MenuItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())

    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    order_items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'items', 'order_items', 'total_price', 'created_at']
        read_only_fields = ['user', 'status', 'total_price', 'created_at']

    def get_order_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        return [
            {
                "menu_item": item.menu_item.name,
                "quantity": item.quantity,
                "price": float(item.menu_item.price) * item.quantity
            }
            for item in order_items
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        order = Order.objects.create(user=user)

        total = 0
        for item_data in items_data:
            menu_item = item_data['menu_item']
            quantity = item_data['quantity']
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
            total += menu_item.price * quantity

        order.total_price = total
        order.save()
        return order
