import json
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SubscriptionPlan

def home(request):
    return render(request, 'subscriptions/home.html', {'plans': SubscriptionPlan.objects.all()})

@login_required
def create_subscription(request, plan_id):
    plan = SubscriptionPlan.objects.get(pk=plan_id)
    # TODO: Request an OAuth token from PayPal and create a subscription using
    # the current PayPal Subscriptions API. Persist the returned subscription ID.
    # Never trust client-provided amount or mark a subscription ACTIVE from a redirect alone.
    return JsonResponse({
        'message': 'PayPal integration is not configured yet.',
        'plan': plan.name,
        'paypal_configured': bool(settings.PAYPAL_CLIENT_ID and settings.PAYPAL_CLIENT_SECRET),
    }, status=501)

@csrf_exempt
def paypal_webhook(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('POST required')
    # TODO: Verify the webhook signature with PayPal before trusting the event.
    # Do not update subscription state based on an unverified webhook payload.
    try:
        event = json.loads(request.body.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return HttpResponseBadRequest('Invalid JSON')
    return JsonResponse({'received': True, 'event_type': event.get('event_type'),
                         'verified': False, 'note': 'Configure PayPal signature verification.'})
