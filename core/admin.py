from core.models import TransactionReceipt
from django.contrib import admin
from .models import TransactionReceipt

@admin.register(TransactionReceipt)
class TransactionReceiptAdmin(admin.ModelAdmin):
    list_display = (
        'payment',
        'made_by',
        'receiver_name',
        'account_number',
        'amount',
        'reference_number',
        'reason_for_payment',
        'status',
        'currency',
        'id'  # This can be removed if unnecessary
    )
    search_fields = ('made_by', 'receiver_name', 'reference_number', 'reason_for_payment')
    list_filter = ('status', 'currency')
    ordering = ('-payment',)  # Sort by payment descending