"""
Data models defining the shape of Order entities.

Uses dataclasses for clean structure and type safety.
"""
from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from datetime import datetime
import uuid

@dataclass
class OrderItem:
    """
    Represents a single line item in an order.
    
    Complexity: O(1)
    """
    sku: str
    quantity: int
    unit_price: Decimal
    name: str

    @property
    def total_price(self) -> Decimal:
        """Calculates line total."""
        return self.quantity * self.unit_price

@dataclass
class Order:
    """
    Represents a customer order.
    
    Complexity: O(N) for item initialization.
    """
    order_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    customer_id: str = ""
    items: List[OrderItem] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    status: str = "PENDING"
    
    # Financial totals (calculated later)
    subtotal: Decimal = Decimal("0.00")
    tax_amount: Decimal = Decimal("0.00")
    final_total: Decimal = Decimal("0.00")