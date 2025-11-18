"""
Global configuration constants for the Nexus System.

Standards:
- All constants must be uppercase.
- Monetary constants must use Decimal strings.
"""
import decimal

# Precision Context for Financial Calculations
MONEY_CONTEXT = decimal.Context(prec=28, rounding=decimal.ROUND_HALF_EVEN)

# Tax Rules
CONF_DEFAULT_TAX_RATE = decimal.Decimal("0.08")  # 8%
CONF_LUXURY_TAX_THRESHOLD = decimal.Decimal("1000.00")
CONF_LUXURY_TAX_RATE = decimal.Decimal("0.12")  # 12%

# System Limits
CONF_MAX_ITEMS_PER_ORDER = 50
CONF_RETENTION_DAYS = 365

# Logging
CONF_LOG_FORMAT = "%(asctime)s - [NEXUS-%(levelname)s] - %(name)s - %(message)s"