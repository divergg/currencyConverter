import datetime
from django.db import models
from django.utils import timezone


class CurrencyRateRequest(models.Model):
    date_of_creation = models.DateTimeField(default=timezone.now, help_text='creation time')
    symbol_from = models.CharField(default=None, max_length=5, help_text='where to convert from')
    symbol_to = models.CharField(default=None, max_length=5, help_text='where to convert to')
    amount_from = models.DecimalField(default=None, max_digits=10, decimal_places=2, help_text='amount to convert')
    amount_to = models.DecimalField(default=None,
                                    null=True,
                                    blank=True,
                                    max_digits=10,
                                    decimal_places=2,
                                    help_text='amount received')
    error_message = models.TextField(default=None, null=True, help_text='side API error')

    class Meta:
        verbose_name = 'CurrencyRateRequest'





