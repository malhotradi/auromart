"""
Standardized logging module for Nexus applications.

Enforces the inclusion of correlation IDs in log messages.
"""
import logging
import sys
from typing import Optional
from src.config.constants import CONF_LOG_FORMAT

def get_nexus_logger(name: str, correlation_id: Optional[str] = None) -> logging.Logger:
    """
    Configures and returns a logger instance adhering to Nexus standards.

    Args:
        name (str): The name of the module requesting the logger.
        correlation_id (Optional[str]): A unique ID to trace the request.

    Returns:
        logging.Logger: Configured logger instance.

    Complexity: O(1) setup cost.
    """
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(CONF_LOG_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # In a real org, we might inject a ContextFilter here.
    # For this demo, we ensure the adapter helps identify the trace.
    if correlation_id:
        logger = logging.LoggerAdapter(logger, {"correlation_id": correlation_id})

    return logger