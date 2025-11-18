"""
Custom Exception hierarchy for Nexus.

Complexity: O(1) for all definitions.
"""

class NexusError(Exception):
    """Base exception class for all Nexus application errors."""
    def __init__(self, message: str, error_code: int = 500):
        self.message = message
        self.error_code = error_code
        super().__init__(f"[Err {error_code}] {message}")


class ValidationError(NexusError):
    """Raised when data validation fails against Nexus standards."""
    def __init__(self, message: str):
        super().__init__(message, error_code=400)


class CalculationError(NexusError):
    """Raised when financial calculations fail (e.g., division by zero)."""
    def __init__(self, message: str):
        super().__init__(message, error_code=422)