"""
Unit tests for the OrderProcessor service.
"""
import pytest
from decimal import Decimal
from src.services.processor import OrderProcessor
from src.core.exceptions import ValidationError
from src.config.constants import CONF_LUXURY_TAX_RATE

def test_process_order_standard():
    """Test a standard order below luxury threshold."""
    processor = OrderProcessor(correlation_id="TEST-001")
    
    items = [
        {"sku": "A100", "name": "Widget", "quantity": 2, "price": "10.00"}
    ]
    
    order = processor.process_order("CUST-1", items)
    
    assert order.status == "PROCESSED"
    assert order.subtotal == Decimal("20.00")
    # 20.00 * 0.08 = 1.60
    assert order.tax_amount == Decimal("1.60")
    assert order.final_total == Decimal("21.60")

def test_process_order_luxury():
    """Test that luxury tax is applied correctly."""
    processor = OrderProcessor(correlation_id="TEST-002")
    
    items = [
        {"sku": "LUX-1", "name": "Gold Bar", "quantity": 1, "price": "2000.00"}
    ]
    
    order = processor.process_order("CUST-2", items)
    
    assert order.subtotal == Decimal("2000.00")
    # 2000 * 0.12 = 240.00
    assert order.tax_amount == Decimal("2000.00") * CONF_LUXURY_TAX_RATE
    assert order.final_total == Decimal("2240.00")

def test_process_invalid_item_count():
    """Test validation error for too many items."""
    processor = OrderProcessor(correlation_id="TEST-003")
    
    # Create a list of 51 items (limit is 50)
    items = [{"sku": f"X{i}", "name": "Item", "quantity": 1, "price": "1.00"} for i in range(51)]
    
    with pytest.raises(ValidationError):
        processor.process_order("CUST-3", items)