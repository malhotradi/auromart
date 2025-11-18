from app.core.config import settings
from app.models.user import User
from app.models.order import Order

class PricingEngine:
    """
    Core business logic for calculating final order prices.
    Includes specific AuraMart rules for VIP tiers and Luxury taxes.
    """
    
    def calculate_total(self, order: Order, user: User) -> float:
        subtotal = sum(item.price * item.quantity for item in order.items)
        tax_total = 0.0
        
        # Rule 1: Calculate Tax based on category
        for item in order.items:
            line_total = item.price * item.quantity
            if item.category == "LUXURY":
                tax_total += line_total * settings.TAX_RATE_LUXURY
            else:
                tax_total += line_total * settings.TAX_RATE_STANDARD
                
        # Rule 2: Apply VIP Discounts (The "Custom" Logic)
        discount_multiplier = 0.0
        if user.tier == "PLATINUM":
            discount_multiplier = 0.15  # 15% off
        elif user.tier == "GOLD":
            discount_multiplier = 0.05  # 5% off
            
        discount_amount = subtotal * discount_multiplier
        
        # Rule 3: Shipping
        shipping_cost = 0.0
        if subtotal < settings.FREE_SHIPPING_THRESHOLD and user.tier != "PLATINUM":
            shipping_cost = 12.50
            
        final_total = subtotal + tax_total + shipping_cost - discount_amount
        
        # Update order object
        order.total_amount = round(final_total, 2)
        order.applied_discount = round(discount_amount, 2)
        
        return order.total_amount
