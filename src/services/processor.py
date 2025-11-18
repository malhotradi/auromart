"""
Main orchestration service for processing orders.
"""
from decimal import Decimal
from typing import List
from src.models.order_types import Order, OrderItem
from src.services.tax_engine import TaxCalculator
from src.core.logger import get_nexus_logger
from src.core.exceptions import ValidationError
from src.config.constants import CONF_MAX_ITEMS_PER_ORDER, MONEY_CONTEXT

class OrderProcessor:
    """
    Orchestrates the lifecycle of an order from validation to finalization.
    """
    
    def __init__(self, correlation_id: str):
        self.correlation_id = correlation_id
        self.logger = get_nexus_logger(__name__, correlation_id)
        self.tax_engine = TaxCalculator(correlation_id)

    def process_order(self, customer_id: str, items_data: List[dict]) -> Order:
        """
        Creates and processes an order.

        Args:
            customer_id (str): Unique customer identifier.
            items_data (List[dict]): Raw dictionary data of items.

        Returns:
            Order: The processed and finalized order object.

        Complexity: O(N) where N is the number of items.
        """
        self.logger.info(f"Starting order processing for customer: {customer_id}")

        # 1. Validation
        if len(items_data) > CONF_MAX_ITEMS_PER_ORDER:
            raise ValidationError(f"Order exceeds max items: {CONF_MAX_ITEMS_PER_ORDER}")

        # 2. Object Creation
        order_items = []
        subtotal = Decimal("0.00")

        for i_data in items_data:
            # Enforce Decimal conversion here for safety
            price = Decimal(str(i_data['price'])).quantize(Decimal("0.01"), context=MONEY_CONTEXT)
            
            item = OrderItem(
                sku=i_data['sku'],
                name=i_data['name'],
                quantity=i_data['quantity'],
                unit_price=price
            )
            order_items.append(item)
            subtotal += item.total_price

        # 3. Create Order Object
        order = Order(
            customer_id=customer_id,
            items=order_items,
            subtotal=subtotal
        )

        # 4. Apply Business Logic (Tax)
        order.tax_amount = self.tax_engine.compute_tax(order.subtotal)
        order.final_total = order.subtotal + order.tax_amount
        order.status = "PROCESSED"

        self.logger.info(f"Order {order.order_id} processed successfully. Total: {order.final_total}")
        return order