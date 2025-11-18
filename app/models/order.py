from typing import List, Optional

class OrderItem:
    def __init__(self, sku: str, price: float, quantity: int, category: str = "GENERAL"):
        self.sku = sku
        self.price = price
        self.quantity = quantity
        self.category = category # GENERAL, ELECTRONICS, LUXURY

class Order:
    def __init__(self, order_id: str, user_id: int, items: List[OrderItem]):
        self.order_id = order_id
        self.user_id = user_id
        self.items = items
        self.status = "PENDING"
        self.total_amount = 0.0
        self.applied_discount = 0.0
