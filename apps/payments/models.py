import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _



class Organization(models.Model):
    """Модель организации"""
    inn = models.CharField(
        _('ИНН'),
        max_length=20,
        unique=True,
        db_index=True
    )
    balance = models.PositiveBigIntegerField(
        _('Баланс'),
        default=0
    )

    def __str__(self):
        return f'Организация: {self.inn}'


class Payment(models.Model):
    """Модель платежа"""
    amount = models.PositiveBigIntegerField(_('Сумма'))
    payer_inn = models.CharField(
        _('ИНН плательщика'),
        max_length=20,
    )
    document_number = models.CharField(
        _('Номер документа'),
        max_length=20
    )
    document_date = models.DateField(_('Дата документа'))


class Operation(models.Model):
    """Модель операции"""
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False,
    )