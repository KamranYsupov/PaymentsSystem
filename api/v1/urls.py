from django.urls import path
from api.v1.payments.views import bank_webhook, organization_balance

urlpatterns = [
    path('webhook/bank/', bank_webhook, name='bank-webhook'),
    path('organizations/<str:inn>/balance/', organization_balance, name='organization-balance'),
]