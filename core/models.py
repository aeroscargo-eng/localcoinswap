# models.py
from django.db import models

class TransactionReceipt(models.Model):
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    made_by = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=50)
    reason_for_payment = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='PENDING')
    currency = models.CharField(max_length=10, default='PHP')  # New field for currency

    def __str__(self):
        return f"Receipt for {self.made_by} - {self.payment} {self.currency}"