from django.conf import settings
from django.db import models

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    paypal_plan_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name} ({self.currency} {self.amount})'

class UserSubscription(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'), ('ACTIVE', 'Active'),
        ('SUSPENDED', 'Suspended'), ('CANCELLED', 'Cancelled'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    paypal_subscription_id = models.CharField(max_length=120, blank=True, db_index=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.plan} - {self.status}'
