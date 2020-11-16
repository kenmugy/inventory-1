from django.contrib import admin
from .models import Stock,StockHistory

# Register your models here.
@admin.register(Stock, StockHistory)
class StockAdmin(admin.ModelAdmin):
    pass
