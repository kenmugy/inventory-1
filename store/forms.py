from django import forms
from .models import Stock, StockHistory

class StockCreateForm(forms.ModelForm):
	
	class Meta:
		model = Stock
		fields = ["item_no", "size", "color", "quantity"]

	# def get_absolute_url(self):
	#     return reverse('list')
		# return reverse('list', kwargs={'pk': self.pk})

	def clean_item_no(self):
		item_no = self.cleaned_data.get("item_no")

		for instance in Stock.objects.all():
			if instance.item_no == item_no:
				raise forms.ValidationError(item_no + " already in Database")
		
		return item_no
	

class StockSearchForm(forms.ModelForm):
	item_no = forms.CharField(required=False)
	color = forms.CharField(required=False)
	export_to_CSV = forms.BooleanField(required=False)
	class Meta:
		model = Stock
		fields = ["item_no", "color"]


class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["item_no", "size", "quantity"]
	

class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quantity', 'issue_to']

	def clean_quantity(self):
		issue_quantity = self.cleaned_data.get("issue_quantity")

		for instance in Stock.objects.all():
			if instance.quantity < issue_quantity:
				raise forms.ValidationError(" Your have less items in the store than your issuing")
		
		return issue_quantity
	

class RecieveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['recieve_quantity']


class ReorderLevelForm(forms.ModelForm):
		
	class Meta:
		model = Stock
		fields = ["reorder_level"]

class StockHistorySearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)
	class Meta:
		model = StockHistory
		fields = [ 'item_no','color', 'start_date', 'end_date']