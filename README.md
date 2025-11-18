# AuraMart Backend API

This is the core backend for the AuraMart E-Commerce platform. It uses a modular architecture separating Models, Services, and API routes.

## 🧠 Gemini Code Assist Demo Tasks

This repository is designed to demonstrate **Codebase Awareness**. 

### Scenario 1: Architectural Understanding
* **Context:** You are new to the team and need to trace data flow.
* **Prompt:** "How is the final price calculated in the `create_order` function? Trace the logic back to the configuration settings."
* **Expected Result:** Gemini should trace from `orders.py` -> `pricing_engine.py` -> `config.py` and explain the relationship between VIP tiers and Tax Rates.

### Scenario 2: Business Logic Inquiry
* **Context:** A Product Manager asks about specific business rules.
* **Prompt:** "What is the tax rate for LUXURY items compared to standard items, and where is this defined?"
* **Expected Result:** Gemini should find the `TAX_RATE_LUXURY` constant in `app/core/config.py` and show how it is used in `PricingEngine`.

### Scenario 3: Feature Expansion (Coding)
* **Context:** You need to add a new VIP tier.
* **Prompt:** "I need to add a new 'DIAMOND' user tier. Update the `User` model to include this option, and update the `PricingEngine` to give Diamond users a 20% discount and free shipping."
* **Expected Result:** Gemini should modify `app/models/user.py` and add a new `elif` block in `app/services/pricing_engine.py`.

### Scenario 4: Documentation Generation
* **Prompt:** "Create a mermaid.js sequence diagram showing the flow of data when `create_order` is called."
