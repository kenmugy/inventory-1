from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
    
    class Meta:
        model = Stock
        fields = ["item_no", "size", "color", "quantity"]

class StockSearchForm(forms.ModelForm):
    item_no = forms.CharField(required=False)
    color = forms.CharField(required=False)
    class Meta:
        model = Stock
        fields = ["item_no", "color"]
