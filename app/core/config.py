import os

class Settings:
    PROJECT_NAME = "AuraMart API"
    VERSION = "2.5.0"
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "aura-mart-super-secret-2025-key-xyz")
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    
    # Business Rules
    TAX_RATE_STANDARD = 0.08
    TAX_RATE_LUXURY = 0.15
    FREE_SHIPPING_THRESHOLD = 100.00
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/auramart_db")

settings = Settings()
