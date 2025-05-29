from rest_framework import serializers

from apps.payments.models import Organization


class BankWebhookSerializer(serializers.Serializer):
    operation_id = serializers.UUIDField()
    amount = serializers.IntegerField(min_value=0)
    payer_inn = serializers.CharField(max_length=20)
    document_number = serializers.CharField(max_length=20)
    document_date = serializers.DateTimeField()


class OrganizationBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['inn', 'balance']
