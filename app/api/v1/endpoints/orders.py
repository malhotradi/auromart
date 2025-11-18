from app.services.pricing_engine import PricingEngine
from app.models.order import Order, OrderItem
from app.models.user import User

# Mock Database lookup
def get_user_by_id(user_id):
    # Simulating a DB fetch
    return User(user_id=user_id, email="demo@auramart.com", tier="GOLD")

pricing_service = PricingEngine()

def create_order(user_id: int, item_list: list):
    """
    POST /orders
    Payload example: [{"sku": "A123", "price": 50.0, "qty": 2}]
    """
    # 1. Fetch User
    user = get_user_by_id(user_id)
    
    # 2. Construct Order Object
    items = [OrderItem(i['sku'], i['price'], i['qty'], i.get('cat', 'GENERAL')) for i in item_list]
    new_order = Order(order_id="ORD-999", user_id=user.id, items=items)
    
    # 3. Calculate Price using the Service
    final_price = pricing_service.calculate_total(new_order, user)
    
    return {
        "order_id": new_order.order_id,
        "user_tier": user.tier,
        "total": final_price,
        "discount_applied": new_order.applied_discount,
        "status": "CREATED"
    }
