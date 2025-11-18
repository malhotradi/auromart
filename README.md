# Nexus Order Management System (NOMS)

## Overview

This repository contains the core logic for the Nexus Order Management System. It is designed as a reference implementation for high-integrity financial transaction processing.

**Target Audience:** Enterprise Python Developers using Gemini Code Assist.

## Organizational Standards (For Code Customization Indexing)

*Observation for AI Training:*

**1. Logging:** Must use src.core.logger.get_nexus_logger and always pass a correlation_id.

**2. Currency:** All monetary values must use decimal.Decimal and the MONEY_CONTEXT from config.

**3. Documentation:** Google-style docstrings are mandatory, and they must include a Complexity: line.

**4. Structure:** Logic is separated into models, services, and core utilities.

## Setup

***1. Create a virtual environment:***

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows


***2. Install requirements:***

pip install -r requirements.txt


***3. Usage***

Run the main entry point:

python main.py


***4. Testing***

Run the test suite:

pytest tests/
