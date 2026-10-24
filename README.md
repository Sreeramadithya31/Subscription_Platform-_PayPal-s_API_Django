# Subscription Platform with PayPal API Using Django 💳

A Django starter project for a subscription service, following the supplied Full Stack Development report's intended Django MVT architecture and PayPal Subscriptions API integration.

## Planned Modules
- Django user accounts and subscription status
- Subscription plan model
- PayPal API integration points
- Webhook endpoint for payment/subscription lifecycle events
- Environment-based configuration

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Create `.env` from `.env.example` and configure PayPal sandbox credentials before implementing live API calls.

## Important
This scaffold intentionally does not pretend to complete PayPal billing. The views include safe integration placeholders. Use PayPal Sandbox first, verify webhook signatures according to PayPal's current documentation, and never store card details locally.
