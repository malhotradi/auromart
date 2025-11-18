"""
Entry point for the Nexus Order Management System.

Simulates an API request handler.
"""
import uuid
import sys
from src.services.processor import OrderProcessor
from src.core.exceptions import NexusError

def main():
    # Simulate an incoming Request ID
    correlation_id = str(uuid.uuid4())
    
    print(f"--- Nexus Order System Initialized [Trace: {correlation_id}] ---")

    # Sample Payload
    sample_payload = [
        {"sku": "TECH-001", "name": "Nexus Laptop", "quantity": 1, "price": "1200.50"},
        {"sku": "ACC-055", "name": "Wireless Mouse", "quantity": 2, "price": "25.00"}
    ]
    
    customer_id = "ENT-CLIENT-8842"

    try:
        # Initialize Service
        processor = OrderProcessor(correlation_id=correlation_id)
        
        # Execute
        order = processor.process_order(customer_id, sample_payload)
        
        # Output Result
        print("\n--- Order Summary ---")
        print(f"Order ID:   {order.order_id}")
        print(f"Status:     {order.status}")
        print(f"Items:      {len(order.items)}")
        print(f"Subtotal:   ${order.subtotal}")
        print(f"Tax:        ${order.tax_amount}")
        print(f"Total:      ${order.final_total}")
        
    except NexusError as e:
        print(f"Error Processing Order: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Critical System Failure: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()