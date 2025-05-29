import loguru
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404

from api.v1.payments.serializers import BankWebhookSerializer, OrganizationBalanceSerializer
from apps.payments.models import Organization, Payment, Operation


@api_view(['POST'])
def bank_webhook(request):
    serializer = BankWebhookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    operation_id = data.pop('operation_id')

    if Operation.objects.filter(id=operation_id).exists():
        return Response(status=status.HTTP_200_OK)

    with transaction.atomic():
        Operation.objects.create(id=operation_id)
        Payment.objects.create(**data)

        organization = get_object_or_404(Organization, inn=data['payer_inn'])
        organization.balance += data['amount']
        organization.save(update_fields=['balance'])

        loguru.logger.info(
            f"Balance updated for Organization INN={organization.inn}: +{data['amount']}, "
            f"new balance={organization.balance}, operation_id={operation_id}"
        )

    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def organization_balance(request, inn):
    organization = get_object_or_404(Organization, inn=inn)
    serializer = OrganizationBalanceSerializer(organization)
    return Response(serializer.data, status=status.HTTP_200_OK)



