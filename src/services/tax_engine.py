"""
Business logic for tax calculation.

Demonstrates organization-specific logic for luxury items.
"""
import decimal
from decimal import Decimal
from src.config.constants import (
    CONF_DEFAULT_TAX_RATE,
    CONF_LUXURY_TAX_RATE,
    CONF_LUXURY_TAX_THRESHOLD,
    MONEY_CONTEXT
)
from src.core.logger import get_nexus_logger
from src.core.exceptions import CalculationError

class TaxCalculator:
    """
    Engine for computing tax based on Nexus fiscal policies.
    """
    
    def __init__(self, correlation_id: str):
        self.logger = get_nexus_logger(__name__, correlation_id)

    def compute_tax(self, subtotal: Decimal) -> Decimal:
        """
        Calculates tax based on the subtotal amount.
        
        Logic:
        - If subtotal > threshold, apply luxury rate.
        - Otherwise, apply default rate.
        
        Args:
            subtotal (Decimal): The net amount before tax.
            
        Returns:
            Decimal: The calculated tax amount.
            
        Raises:
            CalculationError: If the input is negative.

        Complexity: O(1) arithmetic operation.
        """
        if subtotal < Decimal("0.00"):
            self.logger.error(f"Invalid subtotal for tax calculation: {subtotal}")
            raise CalculationError("Cannot calculate tax on negative subtotal.")

        # Enforce strict Decimal context
        decimal.setcontext(MONEY_CONTEXT)

        rate = CONF_DEFAULT_TAX_RATE
        if subtotal > CONF_LUXURY_TAX_THRESHOLD:
            self.logger.info("Applying Luxury Tax Rate.")
            rate = CONF_LUXURY_TAX_RATE
        
        tax_amount = subtotal * rate
        
        # Quantize to 2 decimal places for currency
        return tax_amount.quantize(Decimal("0.01"))